# kle2xy

Python library for turning keyboard-layout-editor.com raw code into X/Y coordinates.

[![Build Status](https://travis-ci.org/skullydazed/kle2xy.svg?branch=master)](https://travis-ci.org/skullydazed/kle2xy)

[![codecov](https://codecov.io/gh/skullydazed/kle2xy/branch/master/graph/badge.svg)](https://codecov.io/gh/skullydazed/kle2xy)

## Usage

```python
from kle2xy import KLE2xy

numpad_code = """["NL","/","*","-"],
["7","8","9",{h:2},"+"],
["4","5","6"],
["1","2","3",{h:2},"Enter"],
[{w:2},"0","."]
"""
layout = KLE2xy(numpad_code)

for row in layout:
    for key in row:
        print('%(name)s:%(x)s,%(y)s\t' % key, end="")
    print()
```

## Installation (coming soon)

```$ pip install kle2xy```

## Contributing

Contributions are always welcome! This project practices TDD, so please ensure
that any new features have 100% code coverage.
