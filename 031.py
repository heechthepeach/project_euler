target = 200
coin = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * (target + 1)
ways[0] = 1

for i in range (0, len(coin)):
	for j in range (coin[i], target+1):
		ways[j] += ways[j - coin[i]]

print(ways[target])
