def isSumFifthEqual(num):
    num_str = str(num)
    sum = 0
    for i in num_str:
        sum += int(i)**5

    if num == sum:
        return True

    return False

sum = 0

for i in range(1000000):
    if isSumFifthEqual(i):
        sum += i

print(sum)