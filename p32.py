pandigitals = set()


numbers = '123456789'


def is_pandigital(string):
    if len(string) > 9:
        return 'stop'

    if len(string) != 9:
        return False

    for number in numbers:
        if number not in string:
            return False

    return True

cap = 10**5

for a in xrange(cap):
    for b in xrange(cap):
        product = a * b
        result = is_pandigital(str(product) + str(a) + str(b))

        if result == 'stop':
            break

        elif result:
            print '%i is PANGIGIGIG' % product
            pandigitals.add(product)


print sum(pandigitals)
