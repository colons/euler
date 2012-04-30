from common import factors

def proper_factor_sum(number):
    factor_set = factors(number)
    factor_set.discard(number)
    s = 0

    for f in factor_set:
        s += f

    return s

amicable = set()

for a in xrange(1, 10000):
    if a not in amicable:
        b = proper_factor_sum(a)

        if b != a and proper_factor_sum(b) == a:
            amicable.add(a)
            amicable.add(b)

t = 0

for i in amicable:
    t += i

print t
