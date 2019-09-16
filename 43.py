from itertools import permutations
numbers = [int(''.join(num)) for num in permutations('0123456789')]
divisors = (2, 3, 5, 7, 11, 13, 17)
def toCheck(num):
    num = str(num)
    for d in range(1, 8):
        if int(num[d:d+3]) % divisors[d-1] != 0:
            return False
    return True
result = sum([number for number in numbers if toCheck(number)])
print(result)
