N, M = [int(x) for x in input().split()]
m = [0] + [int(x) for x in input().split()]

dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(1, N + 1):
    for j in range(0, M + 1):
        dp[i][j] = dp[i - 1][j]
        if m[i] <= j and dp[i - 1][j - m[i]]:
            dp[i][j] = True

inds = []
for j in range(M + 1):
    if dp[N][j]:
        inds.append(j)
print(max(inds))
