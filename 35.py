result = 0

def isPrimeNumber(i):
    for divider in range(2, int(i**0.5)+1):
        if i % divider == 0:
            return False
    return True

for i in range(2, 1000001):
    if isPrimeNumber(i) == False:
        continue
    permutation = str(i)
    for j in range(len(permutation)):
        permutation = permutation[-1] + permutation[:-1]
        if isPrimeNumber(int(permutation)) == False:
            break
    else:
        result += 1
print(result)
