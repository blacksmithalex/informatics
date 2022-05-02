w, h, n = [int(x) for x in input().split()]
l, r = 0, max(w, h) * n

while l + 1 != r:
    a = (l + r) // 2
    if (a // w) * (a // h) < n:
        l = a
    else:
        r = a

print(r)