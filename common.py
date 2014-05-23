alphabet = 'abcdefghijklmnopqrstuvwxyz'


def factors(n):
    d = 1
    fs = set()
    sqrt = int(n**0.5)

    while d <= sqrt:
        if n % d == 0:
            f = n/d
            fs.add(d)
            fs.add(f)

        d += 1

    return fs


def is_prime(number):
    if number == 1 or number < 0:
        return False

    for divisor in xrange(2, int(number**.5)+1):
        if number % divisor == 0:
            return False

    return True


def factorial(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1

    return f


def is_palindrome(word):
    rev = ''
    for l in word:
        rev = l+rev

    if rev == word:
        return True
    else:
        return False


def is_pandigital_string(string, numerals='123456789'):
    if len(string) != 9:
        return False

    for numeral in numerals:
        if numeral not in string:
            return False

    return True


def is_pandigital(number):
    return is_pandigital_string(str(number))
