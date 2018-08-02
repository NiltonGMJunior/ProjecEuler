def main():

    num_list = []
    lim = 1000000
    for i in range(lim):
        num_list.append(str(i + 1))

    num_str = ''.join(num_list)

    lim_exp = 6
    prod = 1

    for i in range(lim_exp + 1):
        prod *= int(num_str[10**i - 1])

    print(prod)

    return

if __name__ == "__main__":
    main()