def sum_mul(n, m):
    if not m>0 or not n>0:
        return 'INVALID'
    return sum([i for i in range(n,m,n)])

def sum_mul_top(n, m):
    return sum(x for x in range(n, m, n)) if m > 0 and n > 0 else 'INVALID'
