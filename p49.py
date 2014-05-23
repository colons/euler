from itertools import permutations

from common import is_prime


four_digit_primes = []


for i in xrange(10**3, 10**4):
    if is_prime(i):
        four_digit_primes.append(i)


for i, a in enumerate(four_digit_primes):
    if a == 1487:  # cited example
        continue

    for b in four_digit_primes[i+1:]:
        c = b + (b - a)
        if c in four_digit_primes:
            ta, tb, tc = [tuple(str(n)) for n in (a, b, c)]
            perms = list(permutations(ta))
            if tb in perms and tc in perms:
                print str(a) + str(b) + str(c)
