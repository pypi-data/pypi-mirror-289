# PartLint

This is a utility for checking KiCad designs for the mistake I keep making: Copying a resistor in the design
and then not updating the MPN or LCSC part number, only the value.

The utility keeps a local SQLite database of LCSC parts from an XLS export JLCPCB provides and checks the
parts in the schematic against the database values and footprints. It also checks if parts that have the
same value and footprint also have the same ordering information.

## Installation

```shell-session
$ pip install partlint
$ partlint update
Downloading new data...
```

## Usage

Just run partlint with the path to the folder the KiCad project is stored in

```shell-session
$ partlint check audio_board
Ref                                                             Value             Footprint    LCSC      Status
--------------------------------------------------------------  ----------------  -----------  --------  ------------
H2, H1, H3, H4                                                  MountingHole_Pad
R12, R11, R14, R13                                              1k                0603         C21190
C6, C5, C6, C5, C5, C37, C6, C18, C12, C9, C13, C57, C48        10uF              0805         C15850    Inconsistent
J11                                                             Conn_01x08
C8                                                              7.5pF             0603         C15850    Value not matching, "10 µF" at LCSC

Found 1 issues

Inconsistent MPN for the same part ('10uF', '0805', 'C'): 
C6, C5, C6, C5, C5, C37, C6: unset
C18, C12, C9, C13, C57, C48: 885012107014
```

## Utilities

There is also the `findres` subcommand for using the database to find the closest matching JLCPCB basic parts for
reaching a specific resistance.

```shell-session
$ partlint findres --footprint 0402 5.1k
Finding closest option for 5.1 kΩ
Value       Error    Combination      Parts
----------  -------  ---------------  --------------
5.1 kΩ      0.00%    5.1 kΩ           C25905
5.1 kΩ      0.00%    1.2 kΩ + 3.9 kΩ  C25862, C51721
5.101 kΩ    0.02%    1 Ω + 5.1 kΩ     C25086, C25905
5.0974 kΩ   -0.05%   5.1 kΩ || 10 MΩ  C25905, C26082
5.09091 kΩ  -0.18%   5.6 kΩ || 56 kΩ  C25908, C25796
5.11 kΩ     0.20%    10 Ω + 5.1 kΩ    C25077, C25905
5.122 kΩ    0.43%    22 Ω + 5.1 kΩ    C25092, C25905
5.07463 kΩ  -0.50%   6.8 kΩ || 20 kΩ  C25917, C25765
5.07412 kΩ  -0.51%   5.1 kΩ || 1 MΩ   C25905, C26083
5.133 kΩ    0.65%    33 Ω + 5.1 kΩ    C25105, C25905
```