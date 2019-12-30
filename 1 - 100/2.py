numbers = [1, 2]

i = 1

while numbers[i - 1] + numbers[i] < 4000000 :
	numbers.append(numbers[i - 1] + numbers[i])

	i += 1

total = 0

for x in numbers :
	if x % 2 == 0 :
		total += x

print(total)