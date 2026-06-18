import pytest 
from project import add_expenses
from project import get_expenses
from project import get_total

def test_get_expenses():
    assert type(get_expenses()) == list

def test_get_total():
    assert type(get_total()) == float

def test_add_expenses():
    assert add_expenses("test", 1.11) is None