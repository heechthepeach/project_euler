def isPandigital(x, y):
	index = range(1,10)
	
	z = x * y
	
	combined = takeApart(x)
	combined.extend(takeApart(y))
	combined.extend(takeApart(z))
	
	combined.sort()
	
	return combined[1:] == index[1:]
	
	
def takeApart(x):
	checkArray = []
	while x > 0:
		subX = x % 10
		checkArray.append(subX)
		x = (x - subX)/10
	return checkArray
	
summation = []

for i in range(100, 9987):
	for j in range(1, 999):
		if isPandigital(i,j):
			if i*j not in summation:
				summation.append(i*j)
print(sum(summation))
