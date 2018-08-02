def isPrime(n):
    if n > 1:
        if n % 2 == 0:
            if n == 2:
                tf = True
            else:
                tf = False
        else:
            tf = True
            i = 3
            while (i < n
                   and tf == True
                   ):
                if n % i == 0:
                    tf = False
                else:
                    i = i + 1
    else:
        tf = False
    return tf

def rotateLeft(s, n):
    if n == 0:
        return s
    return s[n:] + s[:n]

def main():
    lim = 1000000
    cnt = 0
    circ_primes = []
    for i in range(lim):
        s = str(i)
        is_circ_prime = True
        n = 0
        while is_circ_prime:
            if n == len(s):
                break
            try:
                circ_primes.index(int(rotateLeft(s, n)))
            except ValueError:
                is_circ_prime = isPrime(int(rotateLeft(s, n)))
            n += 1
        if is_circ_prime:
            cnt += 1
            circ_primes.append(i)

    print(cnt)
    print(circ_primes)

    return

if __name__ == "__main__":
    main()