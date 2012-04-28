pool = range(1,101)

sum_of_squares = 0
sum_of_pool = 0

for n in pool:
    sum_of_pool += n
    sum_of_squares += n**2

square_of_sum = sum_of_pool ** 2

print square_of_sum - sum_of_squares
