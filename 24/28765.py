from collections import deque

s = open('24_28765.txt').readline()


d = deque()
count_bc = 0
max_len = 0

for ch in s:
    d.append(ch)
    if len(d) > 1:
        if d[-2] + d[-1] == 'BC':
            count_bc += 1

        while count_bc > 180:
            if d[0] + d[1] == 'BC':
                count_bc -= 1
            d.popleft()

        max_len = max(max_len, len(d))

print(max_len)
