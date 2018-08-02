def getDivisorsSum(n):

    if n == 1:
        return 1

    divisors = [1]

    if n % 2 == 0:
        for i in range(n//2 + 1):
            if n % (i + 2) == 0:
                divisors.append(i + 2)
    else:
        for i in range(1, 1 + n//2):
            if n % (i + 2) == 0:
                divisors.append(i + 2)

    sum = 0

    for i in divisors:
        sum += i

    return sum

def main():

    amicable_pairs = []
    lim = 10000
    sum = 0

    for i in range(2, lim):
        try:
            amicable_pairs.index(i)
            continue
        except ValueError:
            test_sum_1 = getDivisorsSum(i)
            test_sum_2 = getDivisorsSum(test_sum_1)
            if  (   test_sum_2 == i
                and test_sum_1 != i
                ):
                amicable_pairs.append(i)
                amicable_pairs.append(test_sum_1)
                sum += i + test_sum_1

    print(amicable_pairs)
    print(sum)

    return

if __name__ == "__main__":
    main()