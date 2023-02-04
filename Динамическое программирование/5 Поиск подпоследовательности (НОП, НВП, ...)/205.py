n = int(input())
a = [int(x) for x in input().split()]
d = [1] * len(a)
for i in range(1, len(a)):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], 1 + d[j])
print(max(d))