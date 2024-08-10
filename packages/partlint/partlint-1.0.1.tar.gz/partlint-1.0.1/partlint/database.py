import io
import math
import os
import re
import sqlite3
import time

import openpyxl
import requests

from partlint.si import si_format


def find_value(description):
    regex = r"([\d.]+)\s*(k|p|u|n|m|µ|G|)\s*(Ohms|Ohm|R|F|H|Ω|A|V|)"
    matches = re.findall(regex, description, re.MULTILINE | re.IGNORECASE)
    units = {}

    multiplier = {
        'K': 1000,
        'k': 1000,
        'm': 0.001,
        'M': 1000000,
        'G': 1000000000,
        'g': 1000000000,
        'µ': 0.000001,
        'u': 0.000001,
        'n': 0.000000001,
        'p': 0.000000000001,
        '': 1,
    }
    unit_norm = {
        'ohms': 'Ohm',
        'ohm': 'Ohm',
        'r': 'Ohm',
        'Ω': 'Ohm',
        'ω': 'Ohm',  # Lowercase Ω
        'f': 'F',
        'h': 'h',
        'a': 'A',
        'v': 'V',
    }
    for num, si, unit in matches:
        if si == '' and unit == '':
            continue
        if unit.lower() not in unit_norm:
            continue
        if si not in multiplier:
            continue
        units[unit_norm[unit.lower()]] = float(num) * multiplier[si]

    priority = ['F', 'h', 'Ohm', 'V', 'A']
    for unit in priority:
        if unit in units:
            return units[unit], unit
    return None


def format_value(val, unit):
    return si_format(float(val), precision=3) + unit


def find_footprint(description):
    smd_names = [
        '0201', '0402', '0603', '0612', '0805', '0815', '1020', '1206', '1210', '1218',
        'SOD-123', 'SOD-323', 'SOD-80', 'SOD-523', 'LL-41', 'LL-34', 'LL-34', 'DO-214AA', 'DO-214AC', 'SMAF',
        'SOT-323', 'SOT-346', 'SOT-363', 'SOT-523', 'SOT-723', 'SOT-89', 'SOT-23-6', 'SOT-323', 'SOT-666',
        'SOT-23-3L', 'SOT-23',
        'SC-89',
        'QFN-24',
    ]
    for test in smd_names:
        if test in description:
            return test

    replacements = {
        'SOIC-16_3.9x9.9mm': 'SOIC-16_150mil',
        'SOIC-16W_7.5x10': 'SOIC-16_300mil',
    }
    for test in replacements:
        if test in description:
            return replacements[test]


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def db_open(database=None):
    if database is None:
        dh = os.path.expanduser(os.environ.get("XDG_DATA_HOME", "~/.local/share"))
        pl = os.path.join(dh, "partlint")
        os.makedirs(pl, exist_ok=True)
        database = os.path.join(pl, "parts.db")
    conn = sqlite3.connect(database)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS lcsc (
        lcsc INTEGER PRIMARY KEY,
        footprint TEXT,
        unit TEXT,
        value FLOAT,
        value_raw TEXT,
        basic_part BOOL,
        mpn TEXT,
        description TEXT
    );
    """
    cur.execute(sql)
    conn.commit()
    return conn


def update_jlcpcb(database=None):
    ch = os.path.expanduser(os.environ.get("XDG_CACHE_HOME", "~/.cache"))
    pl = os.path.join(ch, "partlint")
    os.makedirs(pl, exist_ok=True)
    cache = os.path.join(pl, 'jlcsmt_parts_library.xls')
    refresh = not os.path.isfile(cache)
    if not refresh:
        age = time.time() - os.path.getmtime(cache)
        if age > (60 * 60 * 24):
            refresh = True
    if refresh:
        print("Downloading new data...")
        url = 'https://jlcpcb.com/video/jlcsmt_parts_library.xls'
        response = requests.get(url, stream=True)
        data = response.content
        with open(cache, 'wb') as handle:
            handle.write(data)
    else:
        print("Using cached data...")
        with open(cache, 'rb') as handle:
            data = handle.read()

    xlsx = io.BytesIO(data)

    book = openpyxl.load_workbook(xlsx, read_only=True)
    sheet = book.active

    rownames = []
    result = []
    for row in sheet.iter_rows(values_only=True):
        if len(rownames) == 0:
            rownames = list(row)
            continue
        data = {}
        for i in range(0, len(row)):
            data[rownames[i]] = row[i]

        result.append(data)

    value_whitelist = [
        'Resistor',
        'Capacitor',
        'Inductor'
    ]

    conn = db_open(database)
    for row in result:
        if row['Part #'][0] != 'C':
            continue
        basic = row['Type'] == 'Basic Part'
        lcsc_id = int(row['Part #'][1:])
        value_raw = row['Comment']
        parse = False
        if row['Category'] is not None:
            for needle in value_whitelist:
                if needle in row['Category']:
                    parse = True
                    break
        value = None
        if parse:
            value = find_value(value_raw)
        footprint = row['Package']
        mpn = row['MPN']

        data = {
            'lcsc': lcsc_id,
            'basic': basic,
            'footprint': footprint,
            'unit': value[1] if value is not None else None,
            'value': value[0] if value is not None else None,
            'raw': value_raw,
            'mpn': mpn,
            'description': row['Description'],
        }
        conn.execute(
            'INSERT OR IGNORE INTO lcsc(lcsc, footprint, unit, value, value_raw, basic_part, mpn, description) VALUES (:lcsc, :footprint, :unit, :value, :raw, :basic, :mpn, :description)',
            data)

    conn.commit()
    conn.execute('VACUUM')
    conn.close()
    return result


class PartResult:
    def __init__(self):
        self.lcsc = None
        self.footprint = None
        self.value = None
        self.unit = None
        self.value_raw = None
        self.basic_part = None
        self.mpn = None
        self.description = None

    def compare(self, value, footprint):
        pv = find_value(value)
        if self.unit is not None:
            if pv is None:
                pv = find_value(value + self.unit)
            if not math.isclose(self.value, pv[0]):
                return f'Value not matching, "{format_value(self.value, self.unit)}" at LCSC'
        footprint = find_footprint(footprint)
        if self.footprint is not None:
            if find_footprint(self.footprint) != footprint:
                return f'Footprint not matching, "{self.footprint}" at LCSC'
        return None

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        if self.value is not None:
            return format_value(self.value, self.unit if self.unit != 'Ohm' else 'Ω')
        else:
            return self.value_raw


def find(conn, lcsc=None, mpn=None) -> PartResult | None:
    if isinstance(lcsc, str):
        lcsc = int(lcsc[1:])
    cur = conn.execute('SELECT * FROM lcsc WHERE lcsc = :lcsc', {'lcsc': lcsc})
    row = cur.fetchone()

    if row is None:
        return None
    result = PartResult()
    result.lcsc = 'C' + str(row['lcsc'])
    result.footprint = row['footprint']
    result.value = row['value']
    result.unit = row['unit']
    result.value_raw = row['value_raw']
    result.basic_part = row['basic_part'] != 0
    result.mpn = row['mpn']
    result.description = row['description']
    return result


def find_range(conn, footprint, unit, basic=True):
    cur = conn.execute('SELECT * FROM lcsc WHERE footprint = :footprint AND basic_part = :basic AND unit = :unit', {
        'footprint': footprint,
        'basic': basic,
        'unit': unit
    })
    results = []
    for row in cur.fetchall():
        result = PartResult()
        result.lcsc = 'C' + str(row['lcsc'])
        result.footprint = row['footprint']
        result.value = row['value']
        result.unit = row['unit']
        result.value_raw = row['value_raw']
        result.basic_part = row['basic_part'] != 0
        result.mpn = row['mpn']
        result.description = row['description']

        results.append(result)
    return results


if __name__ == '__main__':
    update_jlcpcb('parts.db')
