N = int(input())
t = [0]*(N + 1)
A = [0]*(N + 1)
B = [0]*(N + 1)
C = [0]*(N + 1)
for i in range(1, N + 1):
    A[i],B[i],C[i] = [int(x) for x in input().split()]

if N == 1:
    print(A[1])
else:
    t[1] = A[1]
    t[2] = min(A[1] + A[2], B[1])
    for i in range(3, N + 1):
        t[i] = min(t[i - 1] + A[i], t[i - 2] + B[i - 1], t[i - 3] + C[i - 2])
    print(t[N])




