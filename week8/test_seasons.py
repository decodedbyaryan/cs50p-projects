import pytest
from seasons import calculate
from datetime import date

def test_corr_min():
    assert calculate(date(2000, 9, 14), date(2026, 6, 14)) == 13541760
    assert calculate(date(2026, 6, 13), date(2026, 6, 14)) == 1440