n = int(input())
if n <= 1:
    print(n)
else:
    cur, prev = 1, 0
    cur_num = 1
    while cur_num != n:
        cur, prev = cur + prev, cur
        cur_num += 1
    print(cur)
