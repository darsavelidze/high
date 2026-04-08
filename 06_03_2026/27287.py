f = open('9_27287.csv')
for i, line in enumerate(f, 1):
    s = sorted([int(x) for x in line.split()])
    counts = [s.count(x) for x in s]
    rep = [x for x in s if s.count(x) > 1]
    unrep = [x for x in s if s.count(x) == 1]
    if counts.count(3) == 6:
        unrep_num = unrep[0]
        if unrep_num <= min(rep):
            print(max(rep))
            break

