N, M = [int(x) for x in input().split()]
m = [0] + [int(x) for x in input().split()]
INF = 10**5

dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(0, M + 1):
        dp[i][j] = dp[i - 1][j]
        if m[i] <= j:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - m[i]] + 1)

if dp[N][M] == INF:
    dp[N][M] = 0
print(dp[N][M])