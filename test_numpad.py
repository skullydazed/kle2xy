# coding=UTF-8
from decimal import Decimal
from kle2xy import KLE2xy

numpad_code = """["Numlock","/","*","-"],
["7\\nHome","8\\nUp","9\\nPgUp",{h:2},"+"],
["4\\nLeft","5","6\\nRight"],
["1\\nEnd","2\\nDown","3\\nPgDn",{h:2},"Enter"],
[{w:2},"0\\nIns",".\\nDel"]
"""


def test_numpad():
    i = KLE2xy(numpad_code)
    # First row
    assert i[0][0]['name'] == 'Numlock'
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('9.525')

    assert i[0][1]['name'] == '/'
    assert i[0][1]['width'] == Decimal('1')
    assert i[0][1]['height'] == Decimal('1')
    assert i[0][1]['x'] == Decimal('28.575')
    assert i[0][1]['y'] == Decimal('9.525')

    assert i[0][2]['name'] == '*'
    assert i[0][2]['width'] == Decimal('1')
    assert i[0][2]['height'] == Decimal('1')
    assert i[0][2]['x'] == Decimal('47.625')
    assert i[0][2]['y'] == Decimal('9.525')

    assert i[0][3]['name'] == '-'
    assert i[0][3]['width'] == Decimal('1')
    assert i[0][3]['height'] == Decimal('1')
    assert i[0][3]['x'] == Decimal('66.675')
    assert i[0][3]['y'] == Decimal('9.525')

    # Second row
    assert i[1][0]['name'] == '7\nHome'
    assert i[1][0]['width'] == Decimal('1')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('9.525')
    assert i[1][0]['y'] == Decimal('28.575')

    assert i[1][1]['name'] == '8\nUp'
    assert i[1][1]['width'] == Decimal('1')
    assert i[1][1]['height'] == Decimal('1')
    assert i[1][1]['x'] == Decimal('28.575')
    assert i[1][1]['y'] == Decimal('28.575')

    assert i[1][2]['name'] == '9\nPgUp'
    assert i[1][2]['width'] == Decimal('1')
    assert i[1][2]['height'] == Decimal('1')
    assert i[1][2]['x'] == Decimal('47.625')
    assert i[1][2]['y'] == Decimal('28.575')

    assert i[1][3]['name'] == '+'
    assert i[1][3]['width'] == Decimal('1')
    assert i[1][3]['height'] == Decimal('2')
    assert i[1][3]['x'] == Decimal('66.675')
    assert i[1][3]['y'] == Decimal('38.1')

    # Third row
    assert i[2][0]['name'] == '4\nLeft'
    assert i[2][0]['width'] == Decimal('1')
    assert i[2][0]['height'] == Decimal('1')
    assert i[2][0]['x'] == Decimal('9.525')
    assert i[2][0]['y'] == Decimal('47.625')

    assert i[2][1]['name'] == '5'
    assert i[2][1]['width'] == Decimal('1')
    assert i[2][1]['height'] == Decimal('1')
    assert i[2][1]['x'] == Decimal('28.575')
    assert i[2][1]['y'] == Decimal('47.625')

    assert i[2][2]['name'] == '6\nRight'
    assert i[2][2]['width'] == Decimal('1')
    assert i[2][2]['height'] == Decimal('1')
    assert i[2][2]['x'] == Decimal('47.625')
    assert i[2][2]['y'] == Decimal('47.625')

    # Fourth row
    assert i[3][0]['name'] == '1\nEnd'
    assert i[3][0]['width'] == Decimal('1')
    assert i[3][0]['height'] == Decimal('1')
    assert i[3][0]['x'] == Decimal('9.525')
    assert i[3][0]['y'] == Decimal('66.675')

    assert i[3][1]['name'] == '2\nDown'
    assert i[3][1]['width'] == Decimal('1')
    assert i[3][1]['height'] == Decimal('1')
    assert i[3][1]['x'] == Decimal('28.575')
    assert i[3][1]['y'] == Decimal('66.675')

    assert i[3][2]['name'] == '3\nPgDn'
    assert i[3][2]['width'] == Decimal('1')
    assert i[3][2]['height'] == Decimal('1')
    assert i[3][2]['x'] == Decimal('47.625')
    assert i[3][2]['y'] == Decimal('66.675')

    assert i[3][3]['name'] == 'Enter'
    assert i[3][3]['width'] == Decimal('1')
    assert i[3][3]['height'] == Decimal('2')
    assert i[3][3]['x'] == Decimal('66.675')
    assert i[3][3]['y'] == Decimal('76.2')

    # Fifth row
    assert i[4][0]['name'] == '0\nIns'
    assert i[4][0]['width'] == Decimal('2')
    assert i[4][0]['height'] == Decimal('1')
    assert i[4][0]['x'] == Decimal('19.05')
    assert i[4][0]['y'] == Decimal('85.725')

    assert i[4][1]['name'] == '.\nDel'
    assert i[4][1]['width'] == Decimal('1')
    assert i[4][1]['height'] == Decimal('1')
    assert i[4][1]['x'] == Decimal('47.625')
    assert i[4][1]['y'] == Decimal('85.725')
