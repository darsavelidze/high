from random import randint
from math import dist

f = open('27_A_25364.txt')
cluster_1 = []
cluster_2 = []
for line in f:
    x, y = map(float, line.replace(',', '.').split())
    if y > 10:
        cluster_1.append([x, y])
    else:
        cluster_2.append([x, y])

print(len(cluster_1))
print(len(cluster_2))

S_list = []
for point_1 in cluster_1:
    S = 0
    for point_2 in cluster_1:
        S += dist(point_1, point_2)
    S_list.append([S, point_1])

print(min(S_list))

S_list = []
for point_1 in cluster_2:
    S = 0
    for point_2 in cluster_2:
        S += dist(point_1, point_2)
    S_list.append([S, point_1])

print(min(S_list))

print(dist([1, 1], [3.8471735, 6.1225014]) * 10000)
print(dist([1, 1], [7.0391548, 12.3587258]) * 10000)

print(chr(randint(128507, 128591 + 1)))
