# coding=UTF-8
from decimal import Decimal
from kle2xy import KLE2xy


def test_1_25u():
    i = KLE2xy('[{h:1.25},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1.25')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-11.90625')


def test_1_50u():
    i = KLE2xy('[{h:1.5},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1.5')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-14.2875')


def test_1_75u():
    i = KLE2xy('[{h:1.75},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1.75')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-16.66875')


def test_2_00u():
    i = KLE2xy('[{h:2},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('2')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-19.05')


def test_2_25u():
    i = KLE2xy('[{h:2.25},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('2.25')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-21.43125')


def test_2_50u():
    i = KLE2xy('[{h:2.5},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('2.5')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-23.8125')


def test_2_75u():
    i = KLE2xy('[{h:2.75},""]')
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('2.75')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-26.19375')


def test_single_row():
    i = KLE2xy('["",{h:2},"",""]')
    # Key 1, 1x1 in upper left
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    # Key 2, 1x2 in upper center
    assert i[0][1]['width'] == Decimal('1')
    assert i[0][1]['height'] == Decimal('2')
    assert i[0][1]['x'] == Decimal('28.575')
    assert i[0][1]['y'] == Decimal('-19.05')
    # Key 3, 1x1 in upper right
    assert i[0][2]['width'] == Decimal('1')
    assert i[0][2]['height'] == Decimal('1')
    assert i[0][2]['x'] == Decimal('47.625')
    assert i[0][2]['y'] == Decimal('-9.525')


def test_double_row():
    i = KLE2xy('["",{h:2},"",""],["",{h:2},"",""]')
    # Key 1, 1x1 in upper left
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')
    # Key 2, 1x2 in upper center
    assert i[0][1]['width'] == Decimal('1')
    assert i[0][1]['height'] == Decimal('2')
    assert i[0][1]['x'] == Decimal('28.575')
    assert i[0][1]['y'] == Decimal('-19.05')
    # Key 3, 1x1 in upper right
    assert i[0][2]['width'] == Decimal('1')
    assert i[0][2]['height'] == Decimal('1')
    assert i[0][2]['x'] == Decimal('47.625')
    assert i[0][2]['y'] == Decimal('-9.525')
    # Key 4, 1x1 in lower left
    assert i[1][0]['width'] == Decimal('1')
    assert i[1][0]['height'] == Decimal('1')
    assert i[1][0]['x'] == Decimal('9.525')
    assert i[1][0]['y'] == Decimal('-28.575')
    # Key 5, 1x2 in lower center
    assert i[1][1]['width'] == Decimal('1')
    assert i[1][1]['height'] == Decimal('2')
    assert i[1][1]['x'] == Decimal('28.575')
    assert i[1][1]['y'] == Decimal('-38.1')
    # Key 6, 1x1 in lower right
    assert i[1][2]['width'] == Decimal('1')
    assert i[1][2]['height'] == Decimal('1')
    assert i[1][2]['x'] == Decimal('47.625')
    assert i[1][2]['y'] == Decimal('-28.575')
