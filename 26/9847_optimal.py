f = open('26_9847.txt')
N = int(f.readline())
timeline = [0] * 1441
for line in f:
    start, end, = map(int, line.split())
    timeline[start] += 1
    timeline[end] -= 1

for i in range(1, len(timeline)):
    timeline[i] += timeline[i - 1]

uniq = [timeline.pop(0)]
for x in timeline:
    if uniq[-1] != x:
        uniq.append(x)

print(uniq.count(643))
