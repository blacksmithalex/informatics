N, S = [int(x) for x in input().split()]
S -= 1
W = [[] for _ in range(N)]
for i in range(N):
    r = [int(x) for x in input().split()]
    for j in range(i + 1, N):
        if r[j] == 1:
            W[i].append(j)
            W[j].append(i)

visited = [False] * N
def dfs(start):
    visited[start] = True
    for v in W[start]:
        if not visited[v]:
            dfs(v)
dfs(S)
print(visited.count(True))