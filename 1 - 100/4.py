def is_palindrome(value) :
	if isinstance(value, (int, float)) :
		value = str(value)

	rev_value = reversed(value)
	if (list(value) == list(rev_value)) :
		return True
	else :
		return False

palindromes = []
for x in reversed(range(100, 999)) :
	for y in reversed(range(100, 999)) :
		if (is_palindrome(x * y)) :
			palindromes.append(x * y)


print(max(palindromes))