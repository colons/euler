from common import factors

target = 500

index = 1
number = 0

while True:
    number += index
    
    fs = factors(number)

    if len(fs) > target:
        print number
        break

    index += 1
