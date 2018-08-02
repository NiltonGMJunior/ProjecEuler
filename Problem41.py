from itertools import permutations

def isPrime(n):

	if (n == 2) or (n == 3):
		return True

	if n < 2:
		return False

	if n % 2 == 0:
		return False

	k = 3

	while k < n:
		if n % k == 0:
			return False
		k += 2

	return True

def main():

	cnt = 0
	n_ref = '987654321'
	prime_found = False

	while not(prime_found):
		n = n_ref[cnt:]
		perms = [''.join(p) for p in permutations(n)]
		print(perms)
		primes = list(filter(lambda x : isPrime(int(x)), perms))
		if primes == []:
			print('No primes found for ' + str(9 - cnt) + ' digits.')
			cnt += 1
		else:
			prime_found = True
			print('Exiting loop')
			break


	return

if __name__ == '__main__':
	main()