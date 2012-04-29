p = 1
n = 2

i = 3

while len(str(n)) < 1000:
    new = p + n
    p = n
    n = new

    i += 1

print i
