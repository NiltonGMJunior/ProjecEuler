def main():

    names_raw = list(open("p022_names.txt"))

    names = names_raw[0].split(',')
    names.sort()

    sum = 0
    cnt = 1

    for i in names:
        sum_letters = 0
        for j in range(1, len(i) - 1):
            sum_letters += ord(i[j].upper()) - (ord('A') - 1)
        sum += sum_letters * cnt
        cnt += 1

    print(sum)

    return

if __name__ == "__main__":
    main()