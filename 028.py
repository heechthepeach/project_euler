i = range(1,1001*1001+1)

index = 0
tuple = 0
sum = 0

print(len(i))

while index < len(i)-1:
	for j in range (1,5):
		index += tuple
		sum += i[index]
	tuple += 2

print (sum-3)
