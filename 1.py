t = 0

for i in range(1000):
    match = False
    for m in [3, 5]:
        if i % m == 0:
            match = True
    
    if match:
        t += i

print t
