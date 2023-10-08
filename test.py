def testf(lst):
    res = 0
    for i in lst:
        res ^= i
    return res

print(testf([1, 2, 3, 4, 5, 1, 2, 3, 4,5,20,20,6,6,7,7]))

x = 50
y = 1
z = x ^ y # z = 32

print('x = ', x)
print('y = ', y)
print('z = ', z)
z ^=y
print('z = ', z)