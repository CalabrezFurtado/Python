from timeconvert import convert
from pytest import raises

def test_ampmhours():

    assert convert('11 AM to 12 PM') == '11:00 to 12:00'
    assert convert('1 AM to 8 PM') == '01:00 to 20:00'

def test_pmpmhours():

    assert convert('11 PM to 12 PM') == '23:00 to 12:00'
    assert convert('1 PM to 8 PM') == '13:00 to 20:00'

def test_errors():

    with raises(ValueError):
        convert('kshsiuahdiwajida')
    with raises(ValueError):
        convert('33 AM to 89 PM')
    with raises(ValueError):
        convert( 'AM 12 to PM 09')

def test_withoutto():
    with raises(ValueError):
        convert('12 PM 12 AM')
