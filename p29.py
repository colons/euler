lower_bound = 2
upper_bound = 100

values = xrange(lower_bound, upper_bound+1)

powers = set()

for a, b in [(a, b) for a in values for b in values]:
    powers.add(a**b)

print len(powers)
