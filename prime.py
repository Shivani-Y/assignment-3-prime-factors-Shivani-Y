"""
prime.py -- Write the application code here
"""
def generate_prime_factors(number):
    """ Code to generate prime factors """
    prime_list = []
    if not isinstance(number, int): #raises an error of function called for any type but integer
        raise ValueError("Only integers can be used in the function")

    if number == 1: #if number 1 then prints a blank list
        print(prime_list)

    return prime_list
