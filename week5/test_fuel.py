import pytest

from fuel import convert
from fuel import gauge

def test_valerror():
    with pytest.raises(ValueError):
        convert("2/1")
        convert("5/3")

def test_zerodiverror():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
        convert("9/0")

def test_per():
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_less_equal_1():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_more_equal_99():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_non_E_F():
    assert gauge(50) == "50%"
    assert gauge(90) == "90%"