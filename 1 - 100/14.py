# if even n -> (n * 3) + 1
# else n -> n / 2

def get_next_in_sequence(number):
	if number % 2 == 0 :
		return number / 2
	else:
		return (number * 3) + 1

def get_steps_for_sequence(number):
	count = 0

	while number != 1:
		number = get_next_in_sequence(number)
		count += 1

	return count

end_int = 1000000     # Integer to end loop at
start_int = 1         # Integer to start loop at
current_max_len = 0   # Current max num of steps
current_max_start = 0 # Current starting number for max num steps

for i in range(start_int, end_int):
	count = get_steps_for_sequence(i)
	
	if count > current_max_len:
		print(count, i)
		current_max_len = count
		current_max_start = i

print(current_max_start)
