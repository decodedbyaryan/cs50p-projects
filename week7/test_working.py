import pytest
import sys
from working import convert

def test_valid():
    assert convert("9:00 AM to 5:00 PM") == '09:00 to 17:00'
    assert convert("9 AM to 5 PM") == '09:00 to 17:00'
    assert convert("12 AM to 12 PM") == '00:00 to 12:00'

def test_invalid():
    with pytest.raises(ValueError):
        convert("13:00 PM to 22:00 pm")
    with pytest.raises(ValueError):
        convert("cat")
