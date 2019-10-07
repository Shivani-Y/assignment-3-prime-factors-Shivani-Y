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
