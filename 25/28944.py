def is_prime(n):
    return len(divisors(n)) == 0

def divisors(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s

def primes(n):
    return {x for x in divisors(n) if is_prime(x)}

for i in range(8_996_452, 10**10):
    p = primes(i)
    for a in p:
        b = i // a
        if b in p and str(a).count('3') == 2 and str(b).count('3') == 2:
            print(i, max(a, b))
            continue