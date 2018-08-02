def main():
    limit = 1000
    sum = 0
    for i in range(limit):
        sum += (i + 1)**(i + 1)

    s = str(sum)

    print(s[-10:])

    return

if __name__ == "__main__":
    main()
