import math

numbers = range(1, 101)

sum_squares = 0
for num in numbers :
	print(num)
	sum_squares += num * num

print(sum_squares)
print(sum(numbers) * sum(numbers))

square_sum = sum(numbers) * sum(numbers)

print (square_sum - sum_squares)