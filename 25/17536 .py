def calc_M(i):
    divs = divisors(i)
    if len(divs) > 0:
        return max(divs) + min(divs)
    else:
        return 0

def divisors(n):
    divs = set()
    for i in range(2, n):
        if n % i == 0:
            divs.add(i)
    return divs

for i in range(800_001, 10**10):
    M = calc_M(i)
    if M % 10 == 4:
        print(i, M)
