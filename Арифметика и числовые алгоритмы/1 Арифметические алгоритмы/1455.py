#В этой задаче не заходит 1, 2 последних теста. Необходимо улучшить факторизацию на простые
from math import sqrt
def isPrime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

n = int(input())
div = {}

d = 2
while d <= n:
    if n % d == 0 and isPrime(d):
        while n % d == 0:
            div[d] = div.get(d, 0) + 1
            n //= d
    d += 1

parts = []
for d in sorted(div):
    if div[d] > 1:
        parts.append(str(d) + '^' + str(div[d]))
    else:
        parts.append(str(d))
print('*'.join(parts))

#------------------------------------#
def primes(n):
    p = [True] * (n + 1)
    p[0], p[1] = False, False
    for i in range(2, n + 1):
        for j in range(i * i, n + 1, i):
            p[j] = False
    return p

n = int(input())
div = {}

for p, val in enumerate(primes(n)):
    if val and n % p == 0:
        while n % p == 0:
            div[p] = div.get(p, 0) + 1
            n //= p

parts = []
for d in sorted(div):
    if div[d] > 1:
        parts.append(str(d) + '^' + str(div[d]))
    else:
        parts.append(str(d))
print('*'.join(parts))






