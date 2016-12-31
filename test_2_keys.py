# coding=UTF-8
from decimal import Decimal
from kle2xy import KLE2xy


def test_1_00u():
    i = KLE2xy('[""],[""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    assert i[1][0]['width'] == Decimal('1')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('9.525')
    assert i[1][0]['y'] == Decimal('-28.575')


def test_1_25u():
    i = KLE2xy('[""],[{w:1.25},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    assert i[1][0]['width'] == Decimal('1.25')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('11.90625')
    assert i[1][0]['y'] == Decimal('-28.575')


def test_1_50u():
    i = KLE2xy('[""],[{w:1.5},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    assert i[1][0]['width'] == Decimal('1.5')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('14.2875')
    assert i[1][0]['y'] == Decimal('-28.575')


def test_1_75u():
    i = KLE2xy('[""],[{w:1.75},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    assert i[1][0]['width'] == Decimal('1.75')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('16.66875')
    assert i[1][0]['y'] == Decimal('-28.575')


def test_2_00u():
    i = KLE2xy('[""],[{w:2},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    assert i[1][0]['width'] == Decimal('2')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('19.05')
    assert i[1][0]['y'] == Decimal('-28.575')


def test_2_25u():
    i = KLE2xy('[""],[{w:2.25},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    assert i[1][0]['width'] == Decimal('2.25')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('21.43125')
    assert i[1][0]['y'] == Decimal('-28.575')


def test_2_50u():
    i = KLE2xy('[""],[{w:2.5},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    assert i[1][0]['width'] == Decimal('2.5')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('23.8125')
    assert i[1][0]['y'] == Decimal('-28.575')


def test_2_75u():
    i = KLE2xy('[""],[{w:2.75},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    assert i[1][0]['width'] == Decimal('2.75')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('26.19375')
    assert i[1][0]['y'] == Decimal('-28.575')
