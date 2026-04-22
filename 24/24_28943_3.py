from collections import deque

s = open('24_28943.txt').readline()

d = deque(maxlen=26)
count_20 = 0
min_len = float('inf')

for i in range(1, len(s)):
    if s[i] in 'AEIOUY':
        if len(d) == 26:
            min_len = min(min_len, i - d[0] + 1)
        d.clear()
    if s[i - 1] + s[i] == '20':
        d.append(i - 1)

print(min_len)
