# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
from prime import generate_prime_factors

def test_data_type_not_integer():

    """Step 1:Checks if the to be evaluated value is not an integer and raise a value error"""
    if not isinstance(generate_prime_factors(2), int):
        raise ValueError("Only integers can be used in the function")

def test_empty_list_on_call_1():
    """Step 2: if 1 called in function, then list is blank"""
    prime_factor_list = []
    if generate_prime_factors(1):
        print(prime_factor_list)

def test_empty_list_on_call_2():
    """Step 3: when function called for 2"""
    i = 2
    prime_factor_list = []
    if (generate_prime_factors(2)%i) == 0:
        prime_factor_list.append(2)
    print(prime_factor_list)

def test_empty_list_on_call_3():
    """Step 4: when function called for 3"""
    i = 2
    prime_factor_list = []
    prime = generate_prime_factors(3) #assigned function to a variale
    while i <= prime:
        if (prime%i) == 0:
            prime_factor_list.append(i)
            prime = prime / i
        else:
            i = i+1

    print(prime_factor_list)
