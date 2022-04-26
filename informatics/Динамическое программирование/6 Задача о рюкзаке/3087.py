N = int(input())
x = [int(i) for i in input().split()]
S = int(input())
INF = 10**8
v = [INF] * (S + 1)
v[0] = 0

for i in range(1, S + 1):
    v[i] = INF
    for j in range(N):
        if S >= x[j] and v[i - x[j]] < v[i]:
            v[i] = v[i - x[j]] + 1

if v[S] == INF:
    print('No solution')
else:
    while S != 0:
        for i in range(N):
            if S - x[i] < 0:
                continue
            if  v[S - x[i]] + 1 == v[S]:
                print(x[i], end = " ")
                S -= x[i]
                break



