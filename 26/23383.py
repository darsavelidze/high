f = open('26_23383.txt')
N = int(f.readline())

data = dict()

for line in f:
    num, point = map(int, line.split())
    if point not in data.keys():
        data[point] = [num]
    else:
        data[point].append(num)

for key in data:
    data[key] = sorted(set(data[key]))

for key, values in data.items():
    max_len = float('-inf')
    cur_len = 1
    for i in range(1, len(values)):
        if values[i] - values[i - 1] == 1:
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        else:
            cur_len = 1

    data[key] = max_len

d = sorted(data.items(), key=lambda x: (-x[1], x[0]))
print(d[0])
