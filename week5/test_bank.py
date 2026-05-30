import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How are you") == 20
    assert value("HI") == 20

def test_non_h():
    assert value("what's up") == 100
    assert value("yo") == 100
    assert value("THERE") == 100

def test_int():
    assert value("0") == 100
    assert value("10") == 100


