import math

number = 600851475143

def is_prime(x) :
	if x >= 2:
		for y in range(2,x):
			if not ( x % y ):
				return False
	else:
		return False
	return True

factors = []
i = 1

while i*i < number :
	if number % i == 0 :
		print(i)
		factors.append(i)

	i += 2

primeFactors = []

for factor in factors :
	print(factor)
	if (is_prime(factor)) :
		primeFactors.append(factor)

print(primeFactors)