a = [[0 for j in range(8)] for i in range(8)]
j_s, i_s = [int(x) for x in input().split()]
a[i_s - 1][j_s - 1] = 1

for i in range(i_s, 8):
    for j in range(8):
        if i - 1 >= 0:
            if j - 1 >= 0 and j + 1 <= 7:
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j + 1]
            elif j - 1 >= 0:
                a[i][j] = a[i - 1][j - 1]
            elif j + 1 <= 7:
                a[i][j] = a[i - 1][j + 1]

print(sum(a[-1]))