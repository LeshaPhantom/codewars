def flick_switch(lst):
    res, state = [], True
    for i in lst:
        if i == 'flick':
            state = not state
        res.append(state)
    return res


def flick_switch_top(lst):
    flick = True
    return [(flick := flick ^ (v == 'flick')) for v in lst]


def main():
    lst = ['codewars', 'flick', 'code', 'wars']
    print(f'{flick_switch(lst)}\n{flick_switch_top(lst)}')


if __name__ == '__main__':
    main()
