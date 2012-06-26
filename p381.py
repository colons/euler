from common import factorial, is_prime

target = 10**8

def get_S(p):
    S = 0
    for k in xrange(1, 5+1):
        S += factorial(p-k)

    return S % p

total = 0

for p in xrange(5, target):
    if is_prime(p):
        total += get_S(p)

print total
