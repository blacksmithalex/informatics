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

def rbs(a, x):
    l = 0
    r = len(a)
    while l + 1 != r:
        c = (l + r) // 2
        if a[c] > x:
            r = c
        else:
            l = c
    return l

N, K = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]

for x in f:
    indl, indr = lbs(a, x), rbs(a, x)
    if a[indl] == x:
        print(indl + 1, indr + 1)
    else:
        print(0)