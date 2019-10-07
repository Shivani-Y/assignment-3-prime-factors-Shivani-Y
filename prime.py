"""
prime.py -- Write the application code here
"""
def generate_prime_factors(number):
    """ Code to generate prime factors """
    prime_factor_list = []
    i = 2
    if not isinstance(number, int):
        raise ValueError("Only integers can be used in the function")

    if number == 1:
        print(prime_factor_list)
    elif (number%i) == 0:
        prime_factor_list.append(2)
    print(prime_factor_list)

    return number
