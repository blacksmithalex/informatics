n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
b = [int(x) for x in input().split()]


dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if a[i - 1] == b[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
print(dp[n][m])