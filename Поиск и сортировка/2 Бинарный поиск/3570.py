a = float(input())
n = int(input())

l = 0
r = 1000
eps = 1e-6
while r - l > eps:
    c = (l + r) / 2
    if c**n < a:
        l = c
    else:
        r = c
print(r)