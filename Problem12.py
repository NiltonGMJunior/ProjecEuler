def numberOfDivisors(num):

    if num == 1:
        return 1
    
    n = 1

    for k in range(1, num):
        if num % k == 0:
            n += 1

    return n

def triangleNumber(num):
    
    triag_number = 0
    
    for i in range(num):
        triag_number += i + 1

    return triag_number

def main():
    
    num = 1
    
    while num > 0:
        num = int(input('Input test number: '))
        print(triangleNumber(num))
        print(numberOfDivisors(num))
    
    return

if __name__ == "__main__":
    main()
