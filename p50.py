from common import is_prime
from sys import exit


cap = 10**6


primes = filter(is_prime, xrange(1, cap))

longest = (0, 0)


for length in xrange(len(primes)):
    for i, start in enumerate(xrange(len(primes) - length)):
        sublist = primes[start:start + length]
        total = sum(sublist)

        if total >= cap:
            if i == 0:
                print longest[1]
                exit()
            else:
                break

        elif is_prime(total) and length > longest[0]:
            longest = (length, total)
