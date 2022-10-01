N = int(input())
costs = [int(x) for x in input().split()]
if N == 1:
    print(costs[0])
else:
    m = [0] * N
    m[0], m[1] = costs[0], costs[1]
    for i in range(2, N):
        m[i] = min(m[i - 1], m[i - 2]) + costs[i]
    print(m[-1])
