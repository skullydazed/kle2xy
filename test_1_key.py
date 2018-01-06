# coding=UTF-8
from decimal import Decimal
from kle2xy import KLE2xy


def test_1_00u():
    i = KLE2xy('[""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_dict():
    i = KLE2xy('{name:"test_1_00u_dict"},[""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i.name == 'test_1_00u_dict'
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_label_style():
    i = KLE2xy('[{a:4},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_label_style_negative():
    i = KLE2xy('[{a:-1},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['label_style'] == 0
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_label_style_too_large():
    i = KLE2xy('[{a:10},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['label_style'] == 9
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_font_size():
    i = KLE2xy('[{f:2},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['label_size'] == 2
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_font_size_negative():
    i = KLE2xy('[{f:-1},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['label_size'] == 1
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_font_size_too_large():
    i = KLE2xy('[{f:10},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['label_size'] == 9
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_keycap_profile():
    i = KLE2xy('[{p:"SA"},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['keycap_profile'] == 'SA'
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_keycap_color():
    i = KLE2xy('[{c:"#232323"},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['keycap_color'] == '#232323'
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_label_color():
    i = KLE2xy('[{t:"#232323"},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['label_color'] == '#232323'
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_x():
    i = KLE2xy('[{x:1},""]')
    assert i.width == Decimal('47.625')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('47.625'),Decimal('28.575'))
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('28.575')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_00u_y():
    i = KLE2xy('[{y:1},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('47.625')
    assert i.size == (Decimal('28.575'),Decimal(47.625))
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-28.575')


def test_1_00u_decal():
    i = KLE2xy('[{d:true},""]')
    assert i.width == Decimal('28.575')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('28.575'), Decimal('28.575'))
    assert i[0][0]['decal'] == True
    assert i[0][0]['width'] == Decimal('1')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('9.525')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_25u():
    i = KLE2xy('[{w:1.25},""]')
    assert i[0][0]['width'] == Decimal('1.25')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('11.90625')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_50u():
    i = KLE2xy('[{w:1.5},""]')
    assert i[0][0]['width'] == Decimal('1.5')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('14.2875')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_1_75u():
    i = KLE2xy('[{w:1.75},""]')
    assert i[0][0]['width'] == Decimal('1.75')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('16.66875')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_2_00u():
    i = KLE2xy('[{w:2},""]')
    assert i[0][0]['width'] == Decimal('2')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('19.05')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_2_25u():
    i = KLE2xy('[{w:2.25},""]')
    assert i[0][0]['width'] == Decimal('2.25')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('21.43125')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_2_50u():
    i = KLE2xy('[{w:2.5},""]')
    assert i[0][0]['width'] == Decimal('2.5')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('23.8125')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_2_75u():
    i = KLE2xy('[{w:2.75},""]')
    assert i[0][0]['width'] == Decimal('2.75')
    assert i[0][0]['height'] == Decimal('1')
    assert i[0][0]['x'] == Decimal('26.19375')
    assert i[0][0]['y'] == Decimal('-9.525')


def test_iso_enter():
    i = KLE2xy('[{x:0.25,a:7,w:1.25,h:2,w2:1.5,h2:1,x2:-0.25},"Enter"]')
    assert i.width == Decimal('33.3375')
    assert i.height == Decimal('28.575')
    assert i.size == (Decimal('33.3375'), Decimal('28.575'))
    assert i[0][0]['isoenter'] == True
    assert i[0][0]['width'] == Decimal('1.25')
    assert i[0][0]['height'] == Decimal('2')
    assert i[0][0]['x'] == Decimal('16.66875')
    assert i[0][0]['y'] == Decimal('-19.05')
