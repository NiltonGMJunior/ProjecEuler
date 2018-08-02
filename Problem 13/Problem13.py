def main():

	data = list(open("num_list.txt"))
	data_num = [int(i) for i in data]
	print(str(sum(data_num))[:10])
	
	return

if __name__ == '__main__':
	main()
