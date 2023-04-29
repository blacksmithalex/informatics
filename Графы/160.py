n = int(input())
W = [[] for _ in range(n)]
for i in range(n):
    line = [int(x) for x in input().split()]
    for j in range(n):
        if line[j] == 1:
            W[i].append(j)
start, end = [int(x) - 1 for x in input().split()]
dist = [-1] * n
path = [[] for _ in range(n)]
dist[start] = 0
path[start] = path[start] + [start]
queue = [start]
while queue:
    u = queue.pop()
    for v in W[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            path[v] = path[u] + [v]
            queue = [v] + queue

if start == end:
    print(0)
elif dist[end] == -1:
    print(-1)
else:
    print(dist[end])
    print(*[x + 1 for x in path[end]])