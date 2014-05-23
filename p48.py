def series(n):
    total = 0

    for i in xrange(1, n+1):
        total += i ** i

    return total

print str(series(1000))[-10:]
