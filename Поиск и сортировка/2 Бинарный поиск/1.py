def f(d, A, N, K):
    prev = A[0]
    count = 1
    for i in range(1, N):
        if A[i] - prev >= d:
            count += 1
            prev = A[i]
    return count >= K

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
l = 1
r = A[-1] - A[0] + 1

while l + 1 != r:
    d = (l + r) // 2
    if f(d, A, N, K):
        l = d
    else:
        r = d
print(l)