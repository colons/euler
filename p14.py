target = 1000000

def time_to_one(n):
    l = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n *= 3
            n += 1
        
        l += 1

    return l

s = 1
results = [0]

while s < target:
    l = time_to_one(s)
    results.append(l)
    s += 1

print results.index(max(results))
