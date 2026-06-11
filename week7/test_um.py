import pytest
from um import count

def test_counts():
    assert count("hey, um, hello, um") == 2
    assert count("um UM Um uM") == 4

def test_zerocount():
    assert count("yummy") == 0
    assert count("mummy") == 0