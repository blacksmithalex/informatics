a = int(input())
b = [int(i) for i in input().split()]
big = - 10e5
bigboy = -10e5 - 1
for s in b:
    if s > big:
        bigboy = big
        big = s
    elif s > bigboy:
        if s != big:
            bigboy = s
print(bigboy)