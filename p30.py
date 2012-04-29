power = 5

i = 2

nines = 0
number = '0'

while nines >= int(number):
    number = number+'9'
    nines += 9**power
    
max_possible_digits = len(number)

total = 0

while len(str(i)) < max_possible_digits:
    istr = str(i)
    
    s = 0
    for l in istr:
        s += int(l)**power

    if s == i:
        total += i
    
    i += 1

print total
