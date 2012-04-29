from common import factors

limit = 28123
# limit = 2812

def is_abundant(n):
    fs = factors(n)
    fs.remove(n)
    
    s = 0

    for f in fs:
        s += f

    if s > n:
        return True
    else:
        return False

abundants = []

n = 1

while n <= limit:
    if is_abundant(n):
        abundants.append(n)

    n += 1

print 'got %i abundants, continuing...' % len(abundants)

sums = set([])

for a in abundants:
    for b in abundants[abundants.index(a):]:
        sums.add(a+b)

print 'got %i sums, continuing...' % len(sums)

n = 1
s = 0

while n <= limit:
    if n not in sums:
        s += n

    n += 1

print s
