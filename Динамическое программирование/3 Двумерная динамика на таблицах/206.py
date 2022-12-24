N, M = [int(x) for x in input().split()]
A = [[1] * M for _ in range(N)]
for i in range(1, N):
    for j in range(1, M):
        A[i][j] = A[i - 1][j] + A[i][j - 1]

print(A[-1][-1])



