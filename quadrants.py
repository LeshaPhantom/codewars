def quadrant(x, y):
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            return 1
        elif x < 0 and y < 0:
            return 3
        elif x < 0:
            return 2
        else:
            return 4
    return 0 
    

def quadrant_top(x, y):
    quadrant = lambda x, y: ((1,2),(4,3))[y<0][x<0]
    return quadrant(x, y)


def main():
    print(quadrant(2, -1))
    print(quadrant_top(2, -1))


if __name__ == '__main__':
    main()