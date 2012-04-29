pool = range(1,21)
print pool

n = 1

while True:
    success = True

    for d in pool:
        if n % d == 0:
            success = False
            break

    if success == True:
        print n
        break
    
    n += 1
