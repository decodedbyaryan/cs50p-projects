import pytest
from numb3rs import validate

def test_correct():
    assert validate("192.168.1.1") == True

def test_wrong():
    assert validate("256.211.1.1") == False
    assert validate("cat") == False