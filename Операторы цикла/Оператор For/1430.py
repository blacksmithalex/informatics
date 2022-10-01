M = int(input())
count = 0
for i in range(1, M + 1):
    for _ in range(i):
        print(i, end = ' ')
        count += 1
        if count == M:
            quit()
