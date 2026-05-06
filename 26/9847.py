f = open('26_9847.txt')
N = int(f.readline())

data = []
for line in f:
    start, end, = map(int, line.split())
    data.append([start, 'start'])
    data.append([end, 'end'])

data = sorted(data, key=lambda x: x)

m = [[0, 0]]

for x in data:
    time, cat = x
    if cat == 'start':
        m.append([time, m[-1][1] + 1])
    else:
        m.append([time, m[-1][1] - 1])

print(max(m, key=lambda x: x[-1]))
print([x for x in m if x[1] == 643])