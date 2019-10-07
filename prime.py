"""
prime.py -- Write the application code here
"""
def generate_prime_factors(number):
    """ Code to generate prime factors """
    prime_list = []
    i = 2
    if not isinstance(number, int): #raises an error of function called for any type but integer
        raise ValueError("Only integers can be used in the function")

    if number == 1: #if number 1 then prints a blank list
        print(prime_list)
    elif number == 2 and number%i == 0: #if number is 2 then prime factor is 2
        prime_list.append(number)
        print(prime_list)
    else:
        while i <= number:
            if (number%i) == 0:
                prime_list.append(i)
                number = number / i
            else:
                i = i+1
        print(prime_list)

    return prime_list
