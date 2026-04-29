f = open('17_28938.txt').readlines()

s = [int(x) for x in f]

max_28 = max([x for x in s if abs(x) % 100 == 28])
m = []
for i in range(len(s) - 2):
    a, b, c = s[i], s[i + 1], s[i + 2]
    cond_1 = (len(str(abs(a))) == 3) + (len(str(abs(b))) == 3) + (len(str(abs(c))) == 3)
    avg = (a + b + c) / 3
    cond_2 = avg > 0
    cond_3 = avg < max_28
    if cond_1 and cond_2 and cond_3:
        m.append(a + b + c)

print(len(m), max(m))
