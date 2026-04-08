def is_prime(x):
    return len(divisors(x)) == 0


def divisors(n):
    divs = set()
    for i in range(2, n**0.5 + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs


def prime_divs(n):
    return [x for x in divisors(n) if is_prime(x)]

