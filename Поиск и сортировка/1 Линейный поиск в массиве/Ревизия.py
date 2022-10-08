N = int(input())
a = [int(x) for x in input().split()]

M, smallM = 2 * 1e9,  2 * 1e9
for x in a:
    if x < M:
        smallM = M
        M = x
    elif x < smallM:
        smallM = x
print(M, smallM)