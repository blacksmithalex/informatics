N = int(input())
a = [int(x) for x in input().split()]
x = int(input())

count = 0
for elem in a:
    if elem == x:
        count += 1
print(count)