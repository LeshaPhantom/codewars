def fake_bin(x):
    lst = []
    for i in x:
        lst.append(0 if int(i)< 5 else 1)
    return ''.join(str(i) for i in lst)

def fake_bin_ref(x):
    return "".join('10'[int(c) <5] for c in x)


fake_bin_top = lambda x: "".join('10'[int(c) <5] for c in x)

def main():
    print(fake_bin("45385593107843568"))
    print(fake_bin_top("45385593107843568"))
    print(fake_bin_ref("45385593107843568"))


if __name__ == '__main__':
    main()
