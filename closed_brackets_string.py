def closed_brackets(s):
    if s == "":
        return True
    tmp = []

    for i in s:
        if i == "(" or i == "J":
            tmp.append(i)
        elif i == ")":
            if len(tmp) == 0:
                return False
            elif "(" in tmp:
                tmp.reverse()
                tmp.pop(tmp.index('('))
                tmp.reverse()
            else:
                tmp.pop()


    t = 0
    for i in range(len(tmp)):
        if tmp[i] == "J" and t == 0:
            continue
        elif tmp[i] == "(":
            t += 1
        else:
            t -= 1
    return not t


def closed_brackets_top(s):
    a, b = 0, 0
    for c in s:
        if c == ")" and b == 0:
            return False
        a = a+1 if c == "(" else a and a-1
        b = b-1 if c == ")" else b+1
    return not a

def main():
    # print(closed_brackets("J(J)"))  # True
    # print(closed_brackets("(JJ)J)J())"))  # True
    # print(closed_brackets("(((JJ(JJ)"))  # True
    # print(closed_brackets("(J(J())(J"))  # True
    # print(closed_brackets("JJ)JJ)"))  # True
    # print(closed_brackets("JJ((J)JJJ"))  # True
    # print(closed_brackets("JJ(J((J())"))
    # print(closed_brackets("J))()"))


    # print(closed_brackets_top("J(J)"))  # True
    print(closed_brackets_top("(JJ)J)J())"))  # True
    # print(closed_brackets_top("(((JJ(JJ)"))  # True
    # print(closed_brackets_top("(J(J())(J"))  # True
    # print(closed_brackets_top("JJ)JJ)"))  # True
    # print(closed_brackets_top("JJ((J)JJJ"))  # True
    # print(closed_brackets_top("JJ(J((J())"))
    # print(closed_brackets_top("J))()"))





if __name__ == '__main__':
    main()
