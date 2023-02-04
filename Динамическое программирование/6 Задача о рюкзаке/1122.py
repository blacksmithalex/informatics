N = int(input())
m = [0] + [int(x) for x in input().split()]
M = sum(m)
if M % 2 != 0:
    print('NO')
else:
    M //= 2
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(1, N + 1):
        for j in range(0, M + 1):
            dp[i][j] = dp[i - 1][j]
            if m[i] <= j and dp[i - 1][j - m[i]]:
                dp[i][j] = True

    if dp[N][M]:
        print('YES')
    else:
        print('NO')