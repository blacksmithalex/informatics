n = int(input())
a = [int(x) for x in input().split()]
x = int(input())

flag = False
for el in a:
    if el == x:
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')