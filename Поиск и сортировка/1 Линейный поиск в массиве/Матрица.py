n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(n)]
Mins, Maxes = [], []

for i in range(n):
    M = 1000
    for j in range(m):
        if a[i][j] < M:
            M = a[i][j]
    Mins.append(M)
for j in range(m):
    M = -1000
    for i in range(n):
        if a[i][j] > M:
            M = a[i][j]
    Maxes.append(M)
count = 0
for i in range(n):
    M = Mins[i]
    for j in range(m):
        if Maxes[j] == M:
            count += 1
print(count)