f = open('26_15_23259 .txt')
N, M = map(int, f.readline().split())

weights = [int(f.readline()) for i in range(N)]
limits = [int(f.readline()) for j in range(M)]

weights = sorted(weights)
limits = sorted(limits)
crews = []
while len(weights) > 0 and len(limits) > 0:
    if weights[0] <= limits[0]:
        crews.append([limits.pop(0), weights.pop(0)])
    else:
        limits.pop(0)


max_weight = max([m for m in weights if m <= crews[-1][0]])
print(len(crews), max_weight)