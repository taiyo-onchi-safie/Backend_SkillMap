import pytest
from q1 import check_sort 

def test_check_sort():
    assert check_sort([1, 2, 3]) == True
    assert check_sort([3, 2, 1]) == True
    assert check_sort([1, 3, 2]) == False
    assert check_sort([]) == False
    assert check_sort([1]) == False
