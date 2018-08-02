def isPrime(n):

	if n < 2:
		return False

	if 	(	n == 2
		or	n == 3
		):
		return True

	if n % 2 == 0:
		return False
	
	k = 3

	while k < n:
		if n % k == 0:
			return False
		k += 2  

	return True

def isTruncPrime(n):
	
	n_ref = str(n)
	n_cut = 0

	while n_cut < len(n_ref):
		if not(isPrime(int(n_ref[n_cut:])) and isPrime(int(n_ref[:len(n_ref) - n_cut]))):
			return False 
		n_cut += 1

	return True

def main():

	cnt = 0 # Truncatable primes counter
	n = 11 # Initial test point
	trunc_primes = []

	while cnt != 11:
		if isTruncPrime(n):
			trunc_primes.append(n)
			cnt += 1
			print(trunc_primes)
			print(cnt)
		n = n + 2


	print(trunc_primes)
	print(sum(trunc_primes))

	return

if __name__ == '__main__':
	main()