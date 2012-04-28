from common import is_prime

target = 10001
n = 2
f = 0

while True:
    if is_prime(n):
        f += 1

        if f == target:
            print n
            break
    
    n += 1
