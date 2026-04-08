from collections import deque

s = open('24_28765.txt').readline()
s = s.replace('BC', 'B*C')
m = s.split('*')

r = []
for i in range(len(m) - 181):
    r.append(sum(map(len, m[i:i+181])))

print(max(r))


