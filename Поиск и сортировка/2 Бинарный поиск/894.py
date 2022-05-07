from math import ceil
vmax, d = [int(x) for x in input().split()]
count = int(input())

distance, growthTime, previousX  = [], [], 0

for _ in range(count):
    X, H, M = [int(x) for x in input().replace(":", " ").split()]
    distance.append(X - previousX)
    previousX = X
    growthTime.append(H * 60 + M)
lastX = previousX

left = 0
right = growthTime[-1]
for j in range(100):
    middle = (right + left) / 2
    time = middle
    for i in range(count-1):
        time += distance[i]/vmax
        if time >= growthTime[i]:
            time += d
    time += distance[-1]/vmax
    if time == growthTime[-1]:
        break
    elif time < growthTime[-1]:
        left = middle
    else:
        right = middle

time = ceil(2 * lastX / vmax + count * d + right)
H = time // 60
M = time % 60

print(str(H).zfill(2) + ":" + str(M).zfill(2))