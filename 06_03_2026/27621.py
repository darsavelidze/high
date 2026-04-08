f = open('9_27621.csv')
for i, line in enumerate(f, 1):
    s = sorted([int(x) for x in line.split()])
    cond_1 = len(set(s)) == len(s)
    cond_2 = (s[-1] - s[0]) == (s[1] + s[2] + s[3])
    if cond_1 and cond_2:
        print(i)
        break

