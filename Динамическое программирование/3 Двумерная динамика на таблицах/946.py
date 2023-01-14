N,M = [int(x) for x in input().split()]

A = [[0 for j in range(M)] for i in range(N)]
A[0][0] = 1

for i in range(1,N):
    for j in range(1,M):
        flag1 = 1
        flag2 = 1
        if i-1<0 or j-2<0:
            flag2 = -1
        if i-2<0 or j-1<0:
            flag1 = -1
        if flag1 == 1 and flag2 == 1:
            A[i][j] = A[i-1][j-2] + A[i-2][j-1]
        if flag1 == 1 and flag2 == -1:
            A[i][j] = A[i-2][j-1]
        if flag1 == -1 and flag2 == 1:
            A[i][j] = A[i-1][j-2]

print(A[N-1][M-1])