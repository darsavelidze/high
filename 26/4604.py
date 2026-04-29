f = open('26_4604.txt')
N = int(f.readline())
data = list(map(int, f.readlines()))
data = sorted(data, key=lambda x: -x)
added = [data.pop(0)]

for i in range(len(data)):
    cur = data[i]
    last = added[-1]
    if abs(last - cur) >= 3:
        added.append(cur)

print(len(added))
added.pop(-1)
m = []
for i in range(len(data)):
    cur = data[i]
    last = added[-1]
    if last - cur >= 3:
        m.append(cur)

print(min(m))
