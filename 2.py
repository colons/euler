fib = [1, 2]

while fib[-1] < 4000000:
    n = fib[-1] + fib[-2]
    fib.append(n)

fib.pop(-1)

t = 0

for n in fib:
    if n % 2 == 0:
        t += n

print t
