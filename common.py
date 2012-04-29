def factors(n):
    d = 1
    fs = []
    sqrt = int(n**0.5)

    while d <= sqrt:
        if n % d == 0:
            f = n/d
            fs.append(d)

            if d == sqrt and f not in fs:
                fs.append(f)
            elif d != sqrt:
                fs.append(f)

        d += 1

    return fs



def is_prime(number):
    if number == 1:
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
