def is_prime(number):
    if number == 1:
        return False

    for divisor in xrange(2, int(number**.5)+1):
        factor = number / divisor
        if number % divisor == 0 and divisor * factor == number:
            return False

    return True
