import numpy

def factorial(n):

    prod = 1
    int_list = [i + 1 for i in range(n)]
    for i in int_list:
        prod *= i

    return prod

if __name__ == "__main__":

    sum = 0

    digits = [int(i) for i in str(factorial(100))]
    
    print(factorial(10))
    print(digits)
    print(numpy.sum(numpy.array(digits)))