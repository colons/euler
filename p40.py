champernowne = []
runs = []


def add_to_champernowne():
    runs.append(None)
    champernowne.extend(list(str(len(runs))))


def d(n):
    while len(champernowne) <= n:
        add_to_champernowne()

    return int(champernowne[n-1])


product = 1


for exp in xrange(6):
    product *= d(10**exp)


print product
