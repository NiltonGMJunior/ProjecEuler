def isTriangle(t):

    n_test1 = (- 1 + (1 + 8*t)**(1/2))/2
    n_test2 = (- 1 - (1 + 8*t)**(1/2))/2

    if type(n_test1) != complex:
        if n_test1 > 0:
            return n_test1 - int(n_test1) == 0
    if type(n_test2) != complex:
        if n_test2 > 0:
            return n_test2 - int(n_test2) == 0

    return False

def main():

    words = list(open("p042_words.txt", 'r'))[0]
    words = words.split(',')
        
    ref = ord('A') - 1
    cnt = 0

    for i in words:
        sum = 0
        i = i[1: len(i) - 1]
        for j in i:
            j = j.upper()
            sum += ord(j) - ref
        if isTriangle(sum):
            cnt += 1
    print(cnt)

    return
    
if __name__ == "__main__":
    main()