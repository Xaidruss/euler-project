# 1 x 1 => 2
# 2 x 2 => 6
# 3 x 3 => 84 
# 
# 
# Write into r & d
# for 3 x 3
# Must have 3 r's 3 d's in any order
# Can use combination formula

import math

def c(total, choose):
	return int((math.factorial(total) / math.factorial(total - choose))/math.factorial(choose))

num = 20
print(c(num * num, num))