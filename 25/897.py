def divisors(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s |= {x // i, i}
    return s

for i in range(1_523_467, 4_157_812 + 1):
    if len(divisors(i)) == 3:
        print(i)
