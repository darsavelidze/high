from collections import deque

s = open('24_28765.txt').readline()

indexes = []
d = deque()

for i in range(1, len(s)):
    if s[i - 1] + s[i] == 'BC':
        indexes.append(i)

left = 0
count = 0
max_len = 0

for i in range(len(indexes) - 181):
    left = indexes[i]
    right = indexes[i + 181] - 1
    max_len = max(max_len, right - left + 1)

print(max_len)