from common import factorial

q = 100
s = 0

for l in str(factorial(q)):
    s += int(l)

print s
