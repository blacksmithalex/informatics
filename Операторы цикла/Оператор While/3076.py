A = int(input())
B = int(input())
while A != B:
    if (A // 2 >= B) and (A % 2 == 0):
        print(':2')
        A //= 2
    else:
        print('-1')
        A -= 1