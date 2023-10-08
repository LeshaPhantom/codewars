def flip(d: str, a: list) -> list:
    a.sort()
    if d != 'R':
        a.reverse()
        return a
    return a


def flip_top(d, a):
    return sorted(a, reverse=d == 'L')


def main():
    print(flip('L', [1, 4, 5, 3, 5]))
    print(flip_top('L', [1, 4, 5, 3, 5]))


if __name__ == '__main__':
    main()
