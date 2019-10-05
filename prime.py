"""
prime.py -- Write the application code here
"""
def generate_prime_factors(to_be_evaluated_value):
    i = 2
    prime_factor_list = []
    while i <= to_be_evaluated_value:
        if (to_be_evaluated_value % i) == 0:
            prime_factor_list.append(i)
            to_be_evaluated_value = to_be_evaluated_value / i
        else:
            i = i + 1
    return prime_factor_list

print (generate_prime_factors(92))
print (generate_prime_factors(9))
print (generate_prime_factors(10))
