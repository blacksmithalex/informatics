N = int(input())
ids = []
for _ in range(N):
    ID, points = [int(x) for x in input().split()]
    ids.append([points, -ID])
ids = sorted(ids, reverse=True)

for var in ids:
    points, ID = var[0], -var[1]
    print(ID, points)

