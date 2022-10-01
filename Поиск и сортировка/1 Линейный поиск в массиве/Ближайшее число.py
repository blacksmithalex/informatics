n = int(input())
a = [int(x) for x in input().split()]
x = int(input())

res = a[0]

for el in a:
    if abs(x - el) < abs(x - res):
        res = el
print(res)