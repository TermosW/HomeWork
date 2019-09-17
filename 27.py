import math
primeRecord = 0
productRecord = 0

def isPrime(numbers):
    if numbers % 2 == 0 or numbers < 0:
        return False
    for i in range(3, math.ceil(math.sqrt(numbers)), 2):
        if numbers % i == 0:
            return False
    return True

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while True:
            if isPrime(n ** 2 + a*n + b):
                n += 1
            else:
                break
        if n > primeRecord:
            primeRecord = n
            productRecord = a*b
print(productRecord)
