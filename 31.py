coins = [1, 2, 5, 10, 20, 50, 100, 200]
table = [0 for i in range(1, 201)]
table[0] = 1
for i in range(0, len(coins), 1):
    for j in range(coins[i], 201, 1):
    	table[j] += table[j-coins[i]]
print(table[200])
