def create_phone_number(s):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*s)


def main():
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(between(1, 4))


if __name__ == '__main__':
    main()
