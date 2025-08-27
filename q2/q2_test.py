import pytest
from q2 import converting_from_binary_to_decimal

def test_converting_from_binary_to_decimal():
    assert converting_from_binary_to_decimal("0") == 0
    assert converting_from_binary_to_decimal("1") == 1
    assert converting_from_binary_to_decimal("1011") == 11
    assert converting_from_binary_to_decimal("000000000000000000000000000000000000000000000000000000000000") == 0