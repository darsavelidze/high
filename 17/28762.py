f = open('17_28762.txt').readlines()

s = [int(x) for x in f]

min_23 = min([x for x in s if x % 23 == 0])
m = []
for i in range(len(s) - 1):
    a, b = s[i], s[i + 1]
    cond_1 = (a % min_23 == 0) + (b % min_23 == 0)
    if cond_1 >= 1:
        m.append(a + b)
print(len(m), max(m))