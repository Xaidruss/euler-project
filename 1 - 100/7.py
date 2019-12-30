def is_prime(x) :
	if x >= 2 :
		for y in range(2, x) :
			if not (x % y) :
				return False
	else:
		return False
	return True

i = 0
primes_found = 0
while primes_found != 10002 :
	if (is_prime(i)) :
		print(primes_found)
		primes_found += 1
	i += 1

print(i)