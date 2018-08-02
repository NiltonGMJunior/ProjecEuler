P_0 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
P_1 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
P_2 = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
P_3 = ['hundred', 'thousand']


def numExtensive(num):

	num_str = str(num)

	if num < 10:
		return P_0[num]
	elif num < 20:
		return P_1[int(num_str[-1])]
	elif num < 100:
		return P_2[int(num_str[0]) - 2] + P_0[int(num_str[-1])]
	elif num < 120:
		return P_0[int(num_str[0])] + ' hundred and ' + P_1[int(num_str[-1])]
	else:
		return P_0[int(num_str[0])] + ' hundred and ' + P_2[int(num_str[1]) - 2] + '-' + P_0[int(num_str[-1])]


def main():

	print(numExtensive(301))

	return

if __name__ == '__main__':
	main()