from jar import Jar

import pytest
jar = Jar()
def test_init():

    assert jar.__init__() == None


def test_str():

    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():

    jar.withdraw(12)
    assert jar.deposit(1) == (['🍪'], 1)

def test_withdraw():

    jar.deposit(3)
    assert jar.withdraw(3) == (['🍪'], 1)

with pytest.raises(ValueError):
    jar.withdraw(1)
    jar.deposit(13)