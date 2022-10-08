a = int(input())
maxy = - 1001
mass = [int(i) for i in input().split()]
for x in range(len(mass)):
    if mass[x] > maxy:
        maxy = mass[x]
        ans = x
print(ans + 1)