a, b = input().split()
b = int(b)
if a == 'North':
    print(0, b)
elif a == 'South':
    print(0, -b)
elif a == 'East':
    print(b, 0)
else:
    print(-b, 0)

