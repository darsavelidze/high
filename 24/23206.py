from collections import deque
f = open('24_23206.txt').readline()
for c in '02468':
    f = f.replace(c,'+')
d = deque()
max_len = 0
count_s = 0
for ch in f:
    if ch == '+':
        count_s = 0
        d.clear()

    d.append(ch)

    if ch == 'S':
        count_s += 1

    if d[0] == '+' and count_s == 35:
        max_len = max(max_len, len(d))

print(max_len)
