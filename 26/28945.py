f = open('26_28945.txt')
N = int(f.readline())

data = []

for line in f:
    start, duration = [int(x) for x in line.split()]
    data.append([start, start + duration])

data = sorted(data, key=lambda x: x[1])

last = data.pop(0)
k = 1
for task in data:
    if task[0] >= last[1]:
        k += 1
        last = task

print(k)

