f = open('26_28945.txt')
N = int(f.readline())

data = []

for line in f:
    start, duration = [int(x) for x in line.split()]
    data.append([start, start + duration])

data = sorted(data, key=lambda x: x[1])

handled = [data.pop(0)]

for task in data:
    if task[0] >= handled[-1][-1]:
        handled.append(task)

print(len(handled))

m = []
handled.pop(-1)
for task in data:
    if task[0] >= handled[-1][-1]:
        m.append(task)

print(10000 - m[-1][-1])
