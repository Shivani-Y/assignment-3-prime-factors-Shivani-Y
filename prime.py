"""
prime.py -- Write the application code here
"""
def generate_prime_factors(number):
    """ Code to generate prime factors """

    if not isinstance(number, int): #raises an error of function called for any type but integer
        raise ValueError("Only integers can be used in the function")
