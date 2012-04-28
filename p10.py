def is_prime(number):
    for divisor in range(2, int(number**.5)+1):
        factor = number / divisor
        if number % divisor == 0 and divisor * factor == number:
            return False

    return True

target = 2000000
n = 2
t = 0

while True:
    if is_prime(n):
        t += n

    if n == target:
        print t
        break
    
    n += 1
