d = dict()
def DEPOSIT(name, sum):
    if name not in d:
        d[name] = sum
    else:
        d[name] += sum
def WITHDRAW(name, sum):
    if name not in d:
        d[name] = -sum
    else:
        d[name] -= sum
def BALANCE(name):
    if name not in d:
        return 'ERROR'
    else:
        return d[name]
def TRANSFER(name1, name2, sum):
    if name1 in d:
        d[name1] -= sum
    else:
        d[name1] = -sum
    if name2 in d:
        d[name2] += sum
    else:
        d[name2] = sum
def INCOME(p):
    for name, sum in d.items():
        if sum > 0:
            d[name] = int(d[name] * (1 + p / 100))
while True:
    try:
        s = input().split()
        if s[0] == 'DEPOSIT':
            DEPOSIT(s[1], int(s[2]))
        if s[0] == 'WITHDRAW':
            WITHDRAW(s[1], int(s[2]))
        if s[0] == 'BALANCE':
            print(BALANCE(s[1]))
        if s[0] == 'TRANSFER':
            TRANSFER(s[1], s[2], int(s[3]))
        if s[0] == 'INCOME':
            INCOME(int(s[1]))
    except:
        break