def ncr(n, r):

    num = 1
    for i in range(n):
        num *= i + 1

    den1 = 1
    for i in range(r):
        den1 *= i + 1

    den2 = 1
    for i in range(n - r):
        den2 *= i + 1

    comb = num/(den1*den2)

    return int(comb)

def main():

    print(ncr(3,2))

    return

if __name__ == "__main__":
    main()
