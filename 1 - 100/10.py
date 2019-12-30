def is_prime(x) :
	if x >= 2:
		for y in range(2,x):
			if not ( x % y ):
				return False
	else:
		return False
	return True

print("Starting")

num = 0;
prime_array = []
for x in range(1, 20000) :
	if (is_prime(x)) :
		prime_array.append(x)

array = list(range(1, 2000000, 2))

print(array)
print(len(prime_array))

for prime in prime_array :
	print(prime)
	i = 1
	while i * prime <= 2000000 :
		if prime in array :
			array.remove(prime)
		i += 1

print(len(array))