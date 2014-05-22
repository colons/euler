from common import is_prime


def rotations(number):
    string = str(number)
    for slice_point in xrange(len(string)):
        yield int(string[slice_point:] + string[:slice_point])


count = 0


for number in xrange(1, 10**6):
    for rotation in rotations(number):
        if not is_prime(rotation):
            break
    else:
        count += 1


print count
