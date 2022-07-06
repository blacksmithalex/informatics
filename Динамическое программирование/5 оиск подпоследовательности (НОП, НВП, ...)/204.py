N = int(input())
a = [int(x) for x in input().split()]
M = int(input())
b = [int(x) for x in input().split()]
LCS = [[0 for j in range(M)] for i in range(N)]

flag = 0
for j in range(M):
    if a[0] == b[j]:
        flag = 1
    LCS[0][j] = flag
flag = 0
for i in range(N):
    if b[0] == a[i]:
        flag = 1
    LCS[i][0] = flag

for i in range(1, N):
    for j in range(1, M):
        if a[i] == b[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[-1][-1])

