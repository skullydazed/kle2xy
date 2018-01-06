# coding=UTF-8
from decimal import Decimal
from kle2xy import KLE2xy

v60_r3_code = """[{w:1.75},"Caps Lock","A","S","D","F","G","H","J","K","L",";","'",{w:2.25},"Enter"]
"""

def test_60_r3():
    i = KLE2xy(v60_r3_code)

    assert i[0][0]['name'] == 'Caps Lock'
    assert i[0][0]['width'] == Decimal('1.75')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('16.66875')
    assert i[0][0]['y'] == Decimal('-9.525')
    assert i[0][0]['column'] == Decimal('0')

    assert i[0][12]['name'] == 'Enter'
    assert i[0][12]['width'] == Decimal('2.25')
    assert i[0][12]['height'] == Decimal('1')
    assert i[0][12]['x'] == Decimal('264.31875')
    assert i[0][12]['y'] == Decimal('-9.525')
    assert i[0][12]['column'] == Decimal('12.75')