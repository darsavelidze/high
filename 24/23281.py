from collections import deque

s = open('24_23281.txt').readline()


d = deque()
count_2025 = 0
count_y = 0
max_len = 0

for ch in s:
    d.append(ch)
    if len(d) > 3:
        if d[-4] + d[-3] + d[-2] + d[-1] == '2025':
            count_2025 += 1
    if ch == 'Y':
        count_y += 1
    while count_y > 80:
        popleft = d.popleft()
        if popleft == 'Y':
            count_y -= 1
        if popleft + d[0] + d[1] + d[2] == '2025':
            count_2025 -= 1
    if count_2025 >= 90:
        max_len = max(max_len, len(d))


print(max_len)

