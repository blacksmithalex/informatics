x = int(input())
p = int(input())
y = int(input())
a = 0
while x < y:
    x = (1 + p / 100) * x
    x = int(100 * x) / 100
    a += 1
print(a)