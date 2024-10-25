import pytest
from main import divide, is_even

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
