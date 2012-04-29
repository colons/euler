def is_prime(number):
    if number == 1:
        return False

    for divisor in xrange(2, int(number**.5)+1):
        if number % divisor == 0:
            return False

    return True

def factorial(n):
    f = 1
    while n != 0:
        f *= n
        n -= 1

    return f
