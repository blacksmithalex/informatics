n, m = [int(x) for x in input().split()]
A = [[0] * n for _ in range(n)]
for _ in range(m):
    i, j = [int(x) - 1 for x in input().split()]
    A[i][j], A[j][i] = 1, 1

for line in A:
    print(*line)