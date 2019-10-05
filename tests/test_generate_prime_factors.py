# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest
from prime import generate_prime_factors

def test_data_type_not_integer():
    """Checks if the to be evaluated value is not an integer and raise a value error"""
    if type(generate_prime_factors(to_be_evaluated_value)) != int:
        pytet.raises(ValueError)
