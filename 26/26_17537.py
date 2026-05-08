f = open('26_17537.txt')
N, M, K = map(int, f.readline().split())
print(N, M, K)
data = [list(map(int, x.split())) for x in f]

m = [10 ** 10] * (K + 1)
for row, seat in data:
    m[seat] = min(m[seat], row)

min_rows = []
for i in range(1, len(m) - 1):
    left, right, = m[i], m[i + 1],
    min_rows.append([min(left, right), i])

print(max(min_rows))
