import argparse
import os.path
import sys
import textwrap
from glob import glob

import tabulate

from partlint import database
from partlint.database import find_footprint
from partlint.schematic import Schematic


def update():
    database.update_jlcpcb()


def findres(value, footprint, limit=10):
    pv = database.find_value(value + "R")
    if pv[1] != 'Ohm':
        sys.stderr.write("Invalid input value\n")
        exit(1)
    value = pv[0]
    print(f"Finding closest option for {database.format_value(value, 'Ω')}")
    conn = database.db_open()
    resistors = database.find_range(conn, footprint, unit='Ohm', basic=True)
    options = []

    def make_option(desired, actual, resistors, op):
        offset = actual - desired
        error = offset / desired * 100
        return actual, error, resistors, op

    # Find closest single resistors
    for r in resistors:
        options.append(make_option(value, r.value, [r], None))

    # Find closest series resistors
    for r1 in resistors:
        if r1.value == 0:
            continue
        for r2 in resistors:
            if r2.value == 0:
                continue
            options.append(make_option(value, r1.value + r2.value, list(sorted([r1, r2])), '+'))

    # Find closest parallel resistors
    for r1 in resistors:
        if r1.value == 0:
            continue
        for r2 in resistors:
            if r2.value == 0:
                continue
            req = (r1.value * r2.value) / (r1.value + r2.value)
            options.append(make_option(value, req, list(sorted([r1, r2])), '/'))

    i = 0
    rows = []
    dedup = []
    for option in sorted(options, key=lambda o: abs(o[1])):
        parts = []
        if option[3] is None:
            key = ['', option[2][0].value]
            resistors = str(option[2][0])
            parts.append(option[2][0].lcsc)
        elif option[3] == '+':
            key = ['+', option[2][0].value, option[2][1].value]
            resistors = f'{option[2][0]} + {option[2][1]}'
            parts.append(option[2][0].lcsc)
            parts.append(option[2][1].lcsc)
        elif option[3] == '/':
            key = ['/', option[2][0].value, option[2][1].value]
            resistors = f'{option[2][0]} || {option[2][1]}'
            parts.append(option[2][0].lcsc)
            parts.append(option[2][1].lcsc)

        if key in dedup:
            continue

        i += 1
        if i > limit:
            break

        dedup.append(key)

        rows.append([
            database.format_value(option[0], 'Ω'),
            f'{option[1]:.2f}%',
            resistors,
            ', '.join(parts)
        ])

    print(tabulate.tabulate(rows, headers=['Value', 'Error', 'Combination', 'Parts']))


def check(path):
    if not os.path.exists(path):
        sys.stderr.write(f"Invalid path: '{path}'\n")
        exit(1)

    db = database.db_open()

    if os.path.isdir(path):
        files = glob(os.path.join(path, '*.kicad_sch'))
    else:
        files = [path]

    if len(files) == 0:
        sys.stderr.write("No schematic files found to check\n")
        exit(1)

    parts = {}
    for file in files:
        schematic = Schematic.open(file)
        for identifier in schematic.parts:
            if identifier not in parts:
                parts[identifier] = []
            parts[identifier].extend(schematic.parts[identifier])

    rows = []
    failures = 0
    errors = []
    for key in parts:
        part_value, part_footprint, part_type = key
        refs = []
        mpns = set()
        lcscs = set()
        for i in parts[key]:
            refs.append(i.ref)
            lcscs.add(i.lcsc)
            mpns.add(i.mpn)
        consistent = True
        if mpns == {None} and lcscs == {None}:
            # Part has no part number info at all
            pass
        else:
            if len(lcscs) != 1:
                variance = {}
                for i in parts[key]:
                    if i.lcsc not in variance:
                        variance[i.lcsc] = []
                    variance[i.lcsc].append(i)
                err = f"Inconsistent LCSC part number for the same part {key}: \n"
                for val in variance:
                    err += ', '.join([p.ref for p in variance[val]]) + ": " + (val if val is not None else "unset") + "\n"
                    lp = database.find(db, val)
                    if lp is not None:
                        err += f'        LCSC part: {lp}\n'
                    else:
                        err += f'        LCSC part not in database\n'
                errors.append(err)
                consistent = False
            if len(mpns) != 1:
                variance = {}
                for i in parts[key]:
                    if i.mpn not in variance:
                        variance[i.mpn] = []
                    variance[i.mpn].append(i.ref)
                err = f"Inconsistent MPN for the same part {key}: \n"
                for val in variance:
                    err += ', '.join(variance[val]) + ": " + (val if val is not None else "unset") + "\n"
                errors.append(err)
                consistent = False
        status = ''
        if not consistent:
            status = 'Inconsistent'

        nums = ''
        partdesc = ''
        if lcscs != {None}:
            nums = ', '.join(map(str, lcscs))

        if len(lcscs) == 1 and lcscs != {None}:
            dbp = database.find(db, lcsc=list(lcscs)[0])
            if dbp is not None:
                partdesc = dbp.description
                match = dbp.compare(part_value, part_footprint)
                if match is not None:
                    status = match
        if len(status):
            failures += 1
        rows.append([', '.join(refs), part_value, find_footprint(part_footprint), nums, textwrap.shorten(partdesc, 64), status])
    print(tabulate.tabulate(rows, headers=['Ref', 'Value', 'Footprint', 'LCSC', 'Description', 'Status']))
    print()
    print(f"Found {failures} issues")
    print()
    for e in errors:
        print(e)
    if failures > 0:
        exit(1)


def main():
    parser = argparse.ArgumentParser(description="KiCad schematic part linting tool")
    subparsers = parser.add_subparsers(dest='command', required=True, title='sub-commands:',
                                       description='These are the subcommands implemented:')

    check_cmd = subparsers.add_parser('check', help='Validate a KiCad schematic')
    check_cmd.add_argument('path', help='Path to the project to validate')

    find_cmd = subparsers.add_parser('findres', help='Find matching basic part resistors')
    find_cmd.add_argument('value', help='Value to find resistors for')
    find_cmd.add_argument('--footprint', '-f', help='Footprint [0603]', default='0603')
    find_cmd.add_argument('--limit', '-n', help='Limit number of results [10]', default=10, type=int)

    subparsers.add_parser('update', help='Fetch the latest parts')
    subparsers.add_parser('help', help='Display this help text')

    kwargs = vars(parser.parse_args())
    cmd = kwargs.pop('command')

    if cmd == 'help':
        parser.print_help()
        exit(0)

    # Dispatch the subcommand to the function with the same name
    globals()[cmd.replace('-', '_')](**kwargs)


if __name__ == '__main__':
    main()
