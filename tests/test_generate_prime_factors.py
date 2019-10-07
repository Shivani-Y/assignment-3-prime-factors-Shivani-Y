# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest
from prime import generate_prime_factors


def test_data_type_not_integer():

    """Step 1:Checks if the to be evaluated value is not an integer and raise a value error"""

    with pytest.raises(ValueError):#raises an error of function called for any type but integer
        if not isinstance(generate_prime_factors(2.2), int):
            raise ValueError("Function only workS for Integers")

def test_empty_list_on_call_1():
    """Step 2: if 1 called in function, then list is blank"""
    prime_factor_list = []
    assert generate_prime_factors(1) == prime_factor_list #checks if 1 then list empty

def test_empty_list_on_call_2():
    """Step 3: if 1 called in function, then list is blank"""
    prime_factor_list = [2]
    assert generate_prime_factors(2) == prime_factor_list #checks if 2 then list has 2 in it
