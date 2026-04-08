from collections import deque

d = deque()

s = '*aa**aa*'
left = 0
best = 0
count = 0

for i in s:
    d.append(i)

    if i == '*':
        count += 1

    while count > 2:
        removed = d.popleft()
        if removed == '*':
            count -= 1

    if count == 2:
        best = max(best, len(d))

print(best)
