from collections import deque

f = open('24_23206.txt').readline()
for c in '02468':
    f = f.replace(c, '+')
max_len = 0
count_s = 0
left = 0
for right in range(len(f)):
    if f[right] == '+':
        left = right
        count_s = 0

    if f[right] == 'S':
        count_s += 1

    if f[left] == '+' and count_s == 35:
        max_len = max(max_len, right - left + 1)


print(max_len)
