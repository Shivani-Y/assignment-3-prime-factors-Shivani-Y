"""
prime.py -- Write the application code here
"""
def generate_prime_factors(number):
    """ Code to generate prime factors """
    prime_factor_list = []
    i = 2
    if not isinstance(number, int):
        ValueError("Only integers can be used in the function")

    while i <= number:
        if (number%i) == 0:
            prime_factor_list.append(i)
            number = number / i
        else:
            i = i+1
    print(prime_factor_list)

    return number
