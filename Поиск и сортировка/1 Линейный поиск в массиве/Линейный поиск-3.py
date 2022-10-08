n = int(input())
a = [int(x) for x in input().split()]
x = int(input())

for i in range(n):
    if a[i] == x:
        print(i + 1)