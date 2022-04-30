def gcd(a, b):
    if a % b == 0 or b % a == 0:
        return min(a, b)
    elif a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)

a = int(input())
b = int(input())
print(gcd(a, b))






