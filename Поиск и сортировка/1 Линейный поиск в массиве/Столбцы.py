X = int(input())
n = int(input())
A = [[int(x) for x in input().split()] for _ in range(n)]

for j in range(n):
    flag = False
    for i in range(n):
        if A[i][j] == X:
            flag = True
            break
    if flag:
        print('YES')
    else:
        print('NO')