f = open('26_4629.txt')
N = f.readline()
data = [int(x) for x in f.readlines()]
for k in (-1, 1):
    data = sorted(data, key=lambda x: x * k)
    print(sum(data[:2500]) // 2 + sum(data[2500:]), end=' ')
