from common import is_prime

def euler_primes(a, b):
    i = 2
    n = 0
    while is_prime(i):
        i = n**2 + a*n + b
        n += 1

    return n

highest_prime_count = 0

a = -1000
while a <= 1000:
    b = -1000
    while b <= 1000:
        pc = euler_primes(a, b)

        if pc > highest_prime_count:
            highest_prime_count = pc
            highest_prime_count_product = a*b

        b += 1
    a += 1

print highest_prime_count_product
