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
    var1, var2 = a[indl], a[indr]
    if var1 - x < x - var2:
        print(var1)
    else:
        print(var2)