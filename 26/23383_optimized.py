f = open('26_23383.txt')
N = int(f.readline())
f = [list(map(int, x.split())) for x in f]
f = sorted(f, key=lambda x: x[0])

data = dict()

# DRY dont repeat yourself
for num, point in f:
    if point not in data:
        data[point] = [1, num, 1]
    else:
        if num - data[point][1] == 1:
            data[point][0] += 1
            data[point][1] = num
            data[point][2] = max(data[point][2], data[point][0])
        elif data[point][1] - num == 0:
            pass
        else:
            data[point][0] = 1
            data[point][1] = num

d = sorted(data.items(), key=lambda x: (-x[1][2], x[0]))
print(d[0][0], d[0][1][2])
