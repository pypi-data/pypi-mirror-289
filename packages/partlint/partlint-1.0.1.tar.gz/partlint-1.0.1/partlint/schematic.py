import os

import sexpdata


class Sym:
    def __init__(self, symbol):
        self.raw = symbol
        self.name = symbol[0].value()
        self.attr = {}
        self.values = []
        self.property = {}

        arrays = ['pad', 'property', 'fp_text', 'fp_line', 'fp_rect', 'fp_circle', 'xy']

        for part in symbol:
            if isinstance(part, sexpdata.Symbol):
                continue
            if isinstance(part, list):
                key = part[0].value()

                if key == 'property':
                    if len(part) == 2:
                        self.property[part[1]] = True
                    else:
                        self.property[part[1]] = part[2]

                if key in arrays:
                    if key not in self.attr:
                        self.attr[key] = []
                    self.attr[key].append(Sym(part))
                else:
                    self.attr[key] = Sym(part)
            else:
                self.values.append(part)

    def __repr__(self):
        values = ' '.join(map(repr, self.values))
        if len(values) > 0:
            return f'<{self.name} {values}>'
        return f'<{self.name}>'

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.values[item]
        if isinstance(item, slice):
            return self.values[item.start:item.stop:item.step]
        return self.attr[item]

    def __contains__(self, item):
        return item in self.attr

    def __len__(self):
        return len(self.values)


class Symbol:
    def __init__(self, sheet, raw: Sym):
        self.sheet = sheet
        prop = raw.property
        self.properties = raw.property

        # Load base data
        self.ref = prop['Reference'] if 'Reference' in prop else 'Ref#'
        self.value = prop['Value'] if 'Value' in prop else None
        self.footprint = prop['Footprint'] if 'Footprint' in prop else None
        self.description = prop['Description'] if 'Description' in prop else None
        self.mpn = prop['MPN'] if 'MPN' in prop else None
        self.lcsc = prop['LCSC'] if 'LCSC' in prop else None

        # Part heuristics
        self.type = 'Unknown'
        lookups = [
            ('Capacitor_SMD:', 'C'),
            ('Resistor_SMD:', 'R'),
            ('Inductor_SMD:', 'L'),
        ]
        for test in lookups:
            if test[0] in self.footprint:
                self.type = test[1]
                break
        footprints = [
            ('_0201_0603', '0201'),
            ('_0402_1005', '0402'),
            ('_0603_1608', '0603'),
            ('_0612_1632', '0612'),
            ('_0805_2012', '0805'),
            ('_0815_2038', '0815'),
            ('_1020_2550', '1020'),
            ('_1206_3216', '1206'),
            ('_1210_3225', '1210'),
            ('_1218_3246', '1218'),
        ]
        for test in footprints:
            if test[0] in self.footprint:
                self.footprint = test[1]
                break

    def __repr__(self):
        return f'<Symbol {self.ref}: {self.value} {self.footprint} [{self.lcsc}]>'


class Schematic:
    def __init__(self):
        self.path = None
        self.uuid = None
        self.sheet = None
        self.symbols = []
        self.parts = {}

    @classmethod
    def open(cls, path):
        inst = cls()
        inst.load(path)
        return inst

    def load(self, path):
        self.path = path
        self.sheet = os.path.basename(path)
        with open(path) as handle:
            raw = sexpdata.load(handle)

        if raw[0].value() != "kicad_sch":
            raise ValueError("Not a valid KiCad schematic file")

        for part in raw[1:]:
            if isinstance(part, sexpdata.Symbol):
                continue
            if isinstance(part, list):
                key = part[0].value()
                if key == "uuid":
                    self.uuid = part[1]
                if key == 'symbol':
                    s = Sym(part)
                    parsed = Symbol(self.sheet, s)
                    if parsed.ref.startswith('#'):
                        continue
                    self.symbols.append(parsed)

        for sym in self.symbols:
            identifier = (sym.value, sym.footprint, sym.type)
            if identifier not in self.parts:
                self.parts[identifier] = []
            self.parts[identifier].append(sym)