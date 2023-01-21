N, M = [int(x) for x in input().split()]
m = [0] + [int(x) for x in input().split()]
c = [0] + [int(x) for x in input().split()]
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(0, M + 1):
        dp[i][j] = dp[i - 1][j]
        if m[i] <= j:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - m[i]] + c[i])

print(max(dp[N]))

