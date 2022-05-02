from math import ceil
def Time(v, d, times, dist):
    if times[0] > dist[0] / v:
        return -1
    else:
        T = dist[0] / v
        for i in range(1, len(times)):
            ti = times[i] - times[i - 1]
            disti = dist[i] - dist[i - 1]
            if ti > disti / v:
                return -1
            T += disti / v
        return 2 * T + len(times) * d
def update1(time):
    h, m = [int(x) for x in time.split(':')]
    return h * 60 + m
def update2(time):
    time = ceil(time)
    time %= 1440
    h, m = time // 60,  time % 60
    return '0' * (2 - len(str(h))) + str(h) + ':' + '0' * (2 - len(str(m))) + str(m)

vmax, d = [int(x) for x in input().split()]
N = int(input())
dist, times = [], []
for _ in range(N):
    disti, timei = input().split()
    dist.append(int(disti))
    times.append(update1(timei))

l = 1
r = vmax + 1
while l + 1 != r:
    v = (l + r) // 2
    t = Time(v, d, times, dist)
    if t != -1:
        l = v
    else:
        r = v

res = Time(2, d, times, dist)
print(update2(res))


