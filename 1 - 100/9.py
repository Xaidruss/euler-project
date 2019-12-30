maximum = 1001

for x in range(1, maximum) :
	for y in range(1, maximum) :
		for z in range(1, maximum) :
			if x + y + z == 1000 :
				if x * x + y * y == z * z :
					print(x, y, z)

print("Finished!")