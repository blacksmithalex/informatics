ip = input().split('.')
if len(ip) == 4:
    flag = True
    for cur in ip:
        if cur.isdigit() == False:
            flag = False
        elif int(cur) < 0 or int(cur) > 255:
            flag = False
    if flag:
        print(1)
    else:
        print(0)
else:
    print(0)
