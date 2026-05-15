f = open('26_1868.txt')

N = int(f.readline())

d = dict()

for line in f:
    row, col = map(int, line.split())
    if row not in d.keys():
        d[row] = [col]
    else:
        d[row].append(col)

for row in d:
    d[row] = sorted(d[row])

for row, col in d.items():
    if len(col) >= 2:
        for i in range(len(col) - 1):
            if col[i + 1] - col[i] == 3:
                print(row, col[i] + 1, col[i] + 2)
