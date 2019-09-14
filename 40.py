start = 1
finish = 1000000
sequence = ""
result = 1

while len(sequence) < finish:
    sequence = sequence + str(start)
    start = start + 1
for i in range(0, 6):
    a = int(sequence[10 ** i - 1])
    result = a*result
print(result)
