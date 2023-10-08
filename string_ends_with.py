def solution(text, ending):
    return text[-len(ending):] == ending


def solution_top(string, ending):
    return string.endswith(ending)


def main():
    solution('abc', 'bc')
    solution('abc', 'd')


if __name__ == '__main__':
    main()
