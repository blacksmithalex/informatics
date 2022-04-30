N, M = [int(x) for x in input().split()] #N - кол-во предметов, M - максимальный вес
m = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

W = [[0 for _ in range(M + 1)] for _ in range(N)]
for i in range(M + 1):
    first_line = W[0]
    if i >= m[0] and m[0] <= M:
        first_line[i] = c[0]

for i in range(1, N):
    for j in range(M + 1):
        if j - m[i] >= 0:
            W[i][j] = max(W[i - 1][j], W[i - 1][j - m[i]] + c[i])
        else:
            W[i][j] = W[i - 1][j]

print(W[-1][-1])
