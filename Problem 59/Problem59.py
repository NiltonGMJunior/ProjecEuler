

def main():

	# Read data

	data = list(open('p059_cipher.txt'))[0].split(',')
	data[-1] = '73' #	Hard coding last element to get rid of line skipping '\n'.

	'''

	Considering key is composed of three lower case 
	characteres, message should be treated in groups 
	of three.

	'''

	while len(data) % 3 != 0:
		data.append('00')

	data = [int(i) for i in data]

	print(data)

	return

if __name__ == '__main__':
	main()