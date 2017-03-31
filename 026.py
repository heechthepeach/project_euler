def recurring_cycle(n, d):
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0
    
maxlength = 0
maxint = 0
for i in range (2,1001):
	index = recurring_cycle(1, i)
	if index > maxlength:
		maxlength = index
		maxint = i
		
print('The maximum int is: ', maxint, ' With the length of: ', maxlength)
