import math
def triangleNumber(num):

	return num * (num + 1) / 2

def isPentagonal(num):

	test = 1 + (1 + 24 * num) ** (1 / 2)

	return test % 6 == 0

def isHexagonal(num):

	test = 1 + (1 + 8 * num) ** (1 / 2)

	return test % 4 == 0

def main():

	test = 285
	cond = False

	while not(cond):
		test += 1
		cond = isPentagonal(triangleNumber(test)) and isHexagonal(triangleNumber(test))

	print(triangleNumber(test))

	return

if __name__ == '__main__':
	main()