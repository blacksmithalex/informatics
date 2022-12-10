n = int(input())
v = sorted([int(x) for x in input().split()])

a = [0 for _ in range(len(v))] #минимальная сумма ниток, необходимых для того, чтобы связать i гвоздей
for i in range(1, n):
    if i > 2:
        a[i] = min(a[i - 1], a[i - 2]) + (v[i] - v[i - 1])
    else:
        a[i] = a[i - 1] + (v[i] - v[i - 1])

print(a[n - 1])