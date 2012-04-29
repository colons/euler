from common import is_prime

big_number = 600851475143

sqr = int(big_number ** 0.5)
f = sqr

while f != 1:
    if big_number % f == 0 and is_prime(f):
        print f
        break

    f -= 1
