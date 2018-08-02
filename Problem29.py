def main():

    base_lower_limit = 2
    base_upper_limit = 100

    exp_lower_limit = 2
    exp_upper_limit = 100

    ref = []

    for a in range(base_lower_limit, base_upper_limit + 1):
        for b in range(exp_lower_limit, exp_upper_limit + 1):
            test = a**b
            try:
                ref.index(test)
            except ValueError:
                ref.append(test)

    print(len(ref))

    return len(ref)

if __name__ == "__main__":
    main()


