def best_friend(txt, a, b):
    return txt.count(a+b) == txt.count(a)


def main():
    print(best_friend('he headed to the store', 'h', 'e'))
    print(best_friend('we found your dynamite', 'd', 'y'))


if __name__ == '__main__':
    main()
