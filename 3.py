from common import is_prime

big_number = 600851475143

sqr = int(big_number ** 0.5)
f = sqr

while True:
    if f == 1:
        break

    if is_prime(f) and big_number % f == 0:
        print f
        break

    f -= 1
