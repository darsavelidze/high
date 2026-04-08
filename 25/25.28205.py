from itertools import combinations
def is_prime(x):
    return len(divs(x))==0
def divs(x):
    a = set()
    for i in range(2,int(x**1/2+1)):
        if x%i==0:
            a.add(i)
            a.add(int(x/i))
    return a
def primes(a):
    return [x for x in a if not divs(x)]
k = 0
a = []
for i in range(2026):
    for j in range(i, 2026):
        if i+j == 2026:
            if is_prime(i) and is_prime(j):
                a.append([min(i,j),max(i,j )])
s = []
for comb in a:
    for i in range(10000000):
        if 20262026 < comb[0]*comb[1]*i:
            s.append(comb[0]*comb[1]*i)
            break
        elif comb[0]*comb[1]*i >= 10**8:
            break
s = sorted(s)
for num in s[:5]:
    a = sorted(primes(divs(num)))
    print(num, a[-1])