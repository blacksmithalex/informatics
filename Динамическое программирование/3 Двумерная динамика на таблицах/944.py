N, M = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(N)]
B = [[0] * M for _ in range(N)]

B[0][0] = A[0][0]
for i in range(1, N):
    B[i][0] = B[i - 1][0] + A[i][0]
for j in range(1, M):
    B[0][j] = B[0][j - 1] + A[0][j]

for i in range(1, N):
    for j in range(1, M):
        B[i][j] = min(B[i][j - 1], B[i - 1][j]) + A[i][j]
print(B[-1][-1])

