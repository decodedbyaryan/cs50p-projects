import pytest
from jar import Jar

def test___init__():
    jar = Jar()
    assert jar.capacity == 12

def test___init__invalid():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(-2)

def test___str__():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2