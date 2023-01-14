n, m = [int(x) for x in input().split()]
costs = [[int(x) for x in input().split()] for i in range(n)]
comm = [[[] for j in range(m)] for i in range(n)]

M = [[0] * m for i in range(n)]
M[0][0] = costs[0][0]

for j in range(1, m):
    M[0][j] = M[0][j - 1] + costs[0][j]
    comm[0][j] = comm[0][j - 1] + ['R']
for i in range(1, n):
    M[i][0] = M[i - 1][0] + costs[i][0]
    comm[i][0] = comm[i - 1][0] + ['D']
for i in range(1, n):
    for j in range(1, m):
        if M[i - 1][j] >= M[i][j - 1]:
            M[i][j] = M[i - 1][j] +  costs[i][j]
            comm[i][j] = comm[i - 1][j] + ['D']
        else:
            M[i][j] = M[i][j - 1] + costs[i][j]
            comm[i][j] = comm[i][j - 1] + ['R']
print(M[-1][-1])
print(*comm[-1][-1])