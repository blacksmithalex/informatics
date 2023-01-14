n, m = [int(x) for x in input().split()]
costs = [[int(x) for x in input().split()] for i in range(n)]
M = [[0] * m for i in range(n)]
M[0][0] = costs[0][0]

for j in range(1, m):
    M[0][j] = M[0][j - 1] + costs[0][j]
for i in range(1, n):
    M[i][0] = M[i - 1][0] + costs[i][0]
for i in range(1, n):
    for j in range(1, m):
        M[i][j] = max(M[i - 1][j], M[i][j - 1]) + costs[i][j]

print(M[-1][-1])