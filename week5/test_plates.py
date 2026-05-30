import pytest
from plates import is_valid

def test_start_alpah():
    assert is_valid("AB") == True
    assert is_valid("CD") == True
    assert is_valid("A1") == False
    assert is_valid("1F") == False

def test_len():
    assert is_valid("BD") == True
    assert is_valid("ABCD12") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_num_end():
    assert is_valid("AB1235") == True
    assert is_valid("ABC123") == True
    assert is_valid("AB12CD") == False
    assert is_valid("CDJ21J") == False

def test_zero_nostart():
    assert is_valid("GH2080") == True
    assert is_valid("FYJI20") == True
    assert is_valid("FY0255") == False

def test_onlyalpnum():
    assert is_valid("DIE1_3") == False
    assert is_valid("DI D34") == False
    assert is_valid("DE.285") == False