f = open('26_17643.txt')
f.readline()
data = [list(map(int, x.split())) for x in f]
avg_data = [x[1] for x in data]
avg = sum(avg_data) / len(avg_data)

rich = [x for x in data if x[1] > avg]

d = dict()

for id, price, stat, in rich:
    sold = 0
    not_sold = 0

    if stat == 0:
        sold = 1
    else:
        not_sold = 1

    if id not in d:
        d[id] = [price, sold, not_sold]
    else:
        d[id][-2] += sold
        d[id][-1] += not_sold

d = sorted(d.values(), key=lambda x: (-x[1], -x[0], x[2]))
print(d[0])
print(d[0][0] * d[0][1])
