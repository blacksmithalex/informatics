words = input().split()
wmax = ''
for w in words:
    if len(w) > len(wmax):
        wmax = w
print(wmax)
print(len(wmax))

