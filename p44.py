pentagonals = []


def p(n):
    return n * ((3 * n) - 1) / 2


def is_pentagonal(n):
    while (not pentagonals) or pentagonals[-1] < n:
        pentagonals.append(p(len(pentagonals)))

    return n in pentagonals


j = 1


d = {}


while True:
    for k in xrange(1, j):
        pj = p(j)
        pk = p(k)

        if is_pentagonal(pj + pk) and is_pentagonal(abs(pj - pk)):
            d[abs(pj - pk)] = (pj, pj)

    if d:
        print min(d)
        break

    j += 1
