# 1 x 1 => 2
# 2 x 2 => 6
# 3 x 3 => 20 
# 
# 
# side length = x
# each route required at least x * 2 sections
# each route has x * 2 choices and can only be x long, we can use choose formula
# 
# x = 1
# total jumps = 2
# 
# x = 2
# total jumps = 4
# 
# x = 3
# total jumps = 6
# 
# x = 20
# total jumps = 40

import math

def c(total, choose):
	return int((math.factorial(total) / math.factorial(total - choose)) / math.factorial(choose))

num = 20
print(c(num * 2, num))