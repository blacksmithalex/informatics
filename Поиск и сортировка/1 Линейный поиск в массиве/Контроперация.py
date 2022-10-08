def minimym(a):
    rez = 1e15
    for x in a:
        if x < rez:
            rez = x
    return rez

def maximym(a):
    rez = -1e15
    for x in a:
        if x > rez:
            rez = x
    return rez

a = [int(x) for x in input().split()][1:]
mina = minimym(a)
maxa = maximym(a)

for i in range(len(a)):
    if a[i] == maxa:
        a[i] = mina
print(' '.join([str(x) for x in a]))