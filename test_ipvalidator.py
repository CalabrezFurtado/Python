from ipvalidator import validate

def test_validate_numbers():

    assert validate("255.255.255.255") == True
    assert validate("25.5.355.255.25.55") == False
    assert validate("255.355.255.255") == False

def test_validate_strorelse():

    assert validate("aaaaa") == False
    assert validate("aaaa__*(*&a") == False
