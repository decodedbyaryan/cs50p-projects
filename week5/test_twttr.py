import pytest
from twttr import shorten


def test_capital():
    assert shorten("ARYAN") == "RYN"
    assert shorten("AGGARWAL") == "GGRWL"

def test_small():
    assert shorten("aryan") == "ryn"
    assert shorten("aggarwal") == "ggrwl"

def test_allcap():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_number():
    assert shorten("12") == "12"
    assert shorten("99") == "99"

def test_mix():
    assert shorten("abc123") == "bc123"
    assert shorten("aeiou225") == "225"