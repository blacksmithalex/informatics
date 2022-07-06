n = int(input())
a = [int(x) for x in input().split()]
v = [0] * n

for i in range(n):
    v[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            v[i] = max(v[i], v[j] + 1)
print(max(v))
