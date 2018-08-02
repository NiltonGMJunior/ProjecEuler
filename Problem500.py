

def main():


	d = lambda n : len(list(filter(lambda x : n % x == 0 , list(range(1, n + 1)))))

	n = 1
	t = 0

	while t < 100:

		n += 1

		t = d(n)

	print(n)

	return

if __name__ == '__main__':
	main()