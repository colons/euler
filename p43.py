from itertools import permutations


numerals = '1234567890'

divisors = [2, 3, 5, 7, 11, 13, 17]


def has_property(string):
    for i, n in enumerate(xrange(1, 8)):
        number = int(string[n:n+3])
        if number % divisors[i] != 0:
            return False

    return True


total = 0


for permutation in permutations(numerals):
    string = ''.join(permutation)
    if has_property(string):
        total += int(string)

print total
