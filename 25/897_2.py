def divisors(x):
    s = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            s |= {x // i, i}
    return s

for i in range(int(1_523_467**0.25), int(4_157_812**0.25)):
    i = i ** 4
    if len(divisors(i)) == 5:
        print(i, sorted(divisors(i))[-2])

