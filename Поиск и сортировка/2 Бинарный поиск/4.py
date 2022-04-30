def lbs(a, x):
    l = -1
    r = len(a) - 1
    while l + 1 != r:
        c = (l + r) // 2
        if a[c] < x:
            l = c
        else:
            r = c
    return r

N, K = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]

for x in f:
    if a[lbs(a, x)] == x:
        print('YES')
    else:
        print('NO')