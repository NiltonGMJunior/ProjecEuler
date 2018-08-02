def isPrime(n):

	if n < 2:
		return False
	elif (n == 2) or (n == 3):
		return True
	elif n % 2 == 0:
		return False

	k = 3

	while k < n:
		if n % k == 0:
			return False
		k += 2

	return True

def primeDiv(n):

	div = []
	tf1, tf2 = True, True

	ref = n

	while tf1 == True:
		if ref % 2  == 0:
			ref /= 2
			div.append(2)
		else:
			tf1 = False

	while tf2 == True:
		p = 3
		if (ref % p == 0) and (isPrime(p) == True):
			ref /= p
			div.append(p)
		else:
			p += 2

		if ref == 1:
			tf2 = False

	return div

def main():

	# consec = 0
	# n = 646

	# while consec < 4:

	print(primeDiv(14))

	return

if __name__ == '__main__':
	main()