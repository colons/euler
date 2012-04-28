def nine(target):
    pool = xrange(target)

    for c in pool:
        for b in pool:
            if b >= c:
                break

            for a in pool:
                if a >= b:
                    break

                if a**2 + b**2 == c**2 and a + b + c == target:
                    return a * b * c

print nine(1000)
