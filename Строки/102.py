def isdigit(c):
    vars = '0123456789'
    if c in vars:
        return True
    else:
        return False

c = input()
if isdigit(c):
    print('yes')
else:
    print('no')
