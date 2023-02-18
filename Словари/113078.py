nums, cand = {}, {}
n = int(input())
for _ in range(n):
    state, m = input().split()
    nums[state] = int(m)
n = int(input())
for _ in range(n):
    state, c = input().split()
    if state in cand:
        alls = cand[state]
        alls[c] = alls.get(c, 0) + 1
    else:
        cand[state] = {c: 1}

for state in cand:
    cs = cand[state]
    M = max(cs.values())
    mcands = sorted([c for c in cs if cs[c] == M])
    if len(mcands) == 1:
        votes = sum(cs.values())
        cs[mcands[0]] += (nums[state] - votes)
    else:
        for c in cs:
            if c == mcands[0]:
                cs[c] = nums[state]
            else:
                cs[c] = 0
res = {}
for state in cand:
    cs = cand[state]
    for c in cs:
        res[c] = res.get(c, 0) + cs[c]
last = []
for var in res:
    last.append([-res[var], var])
last = sorted(last)

for var in last:
    print(var[1], -var[0])
