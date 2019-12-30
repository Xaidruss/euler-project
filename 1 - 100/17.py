def convert_to_string(number):
	conversions = {0: 4, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
	
	return conversions[number]

value = 0
for i in range(1, 1001):
	value += convert_to_string(i)

print(value)