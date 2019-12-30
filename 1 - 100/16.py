# Find power
# Convert to string
# Add digits

num = 2
power = 1000

value = 1
for i in range(0, power):
	value *= num

value_list = [int(d) for d in str(value)]

value = 0
for i in value_list:
	value += i

print(value)