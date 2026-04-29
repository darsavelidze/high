f = open('26_9756.txt')
N = int(f.readline())
data = [list(map(int, x.split())) for x in f.readlines()]
data = sorted(data, key=lambda x: (x[1], x[0]))
viewed = [data.pop(0)]

for i in range(len(data)):
    last_time = viewed[-1][1]
    start_time = data[i][0]

    if start_time >= last_time:
        viewed.append(data[i])

print(len(viewed))

viewed.pop(-1)
m = []
last_time = viewed[-1][1]

for i in range(len(data)):
    start_time = data[i][0]

    if start_time >= last_time:
        m.append(data[i])

print(m)
