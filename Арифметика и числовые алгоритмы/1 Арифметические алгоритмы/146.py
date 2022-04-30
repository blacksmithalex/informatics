def gcd(a, b):
    if a % b == 0 or b % a == 0:
        return min(a, b)
    elif a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)

def Toirreducible(a, b):
    ab_gcd = gcd(a, b)
    return a // ab_gcd, b // ab_gcd

a, b, c, d = [int(x) for x in input().split()]
a, b = Toirreducible(a, b)
c, d = Toirreducible(c, d)

lcm_bd = b * d // gcd(b, d)
factor1, factor2 = lcm_bd // b, lcm_bd // d
num = a * factor1 + c * factor2

num, lcm_bd = Toirreducible(num, lcm_bd)
print(num, lcm_bd)








