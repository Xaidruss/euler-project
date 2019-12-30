numbers = []

i = 1
while i < 1000 :
	if i % 3 == 0 or i % 5 == 0 :
		numbers.append(i)

	i += 1

total = 0

for num in numbers :
	total += num

print(total)