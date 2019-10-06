# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
from prime import generate_prime_factors

def test_data_type_not_integer():

    """Step 1:Checks if the to be evaluated value is not an integer and raise a value error"""
    if not isinstance(generate_prime_factors(2), int):
        raise ValueError("Only integers can be used in the function")
