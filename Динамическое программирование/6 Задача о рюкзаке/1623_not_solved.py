INF = 10**9
A, B, C = [int(x) for x in input().split()]
N = int(input())
d = [0] + [int(x) for x in input().split()]
if A > C:
    print(A)
    print(0)
elif C - A >= B:
    print(A + B)
    print(-1)
else:
    dp = [[False] * B for _ in range(N + 1)]
    goods = [[[] for _ in range(B)]for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(1, N + 1):
        for j in range(0, B):
            dp[i][j] = dp[i - 1][j]
            goods[i][j] = goods[i - 1][j]
            if d[i] <= j and dp[i - 1][j - d[i]]:
                dp[i][j] = True
                goods[i][j] = goods[i - 1][j - d[i]] + [i]
    S = C - A + 1
    extra = INF
    for j in range(S, B):
        if dp[N][j]:
            extra = j
            break
    if extra == INF:
        print(A + B)
        print(-1)
    else:
        print(A + extra)
        g = goods[N][extra]
        print(len(g), *g)

