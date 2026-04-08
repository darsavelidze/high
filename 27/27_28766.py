from math import dist
def calc_centers(cluster):
    min_sum = 10**10
    center = None
    for p1 in cluster:
        cur_sum = 0
        for p2 in cluster:
            cur_sum += dist(p1[:2], p2[:2])
        if cur_sum < min_sum:
            min_sum = cur_sum
            center = p1

    return center




f = open('27_A_28766.txt')

cluster_1 = []
cluster_2 = []
cluster_3 = []

for line in f:
    new_line = line.replace(',', '.').split()
    point = [float(x) for x in new_line[:2]] + new_line[-1:]
    if point[1] < 10:
        cluster_1.append(point)
    else:
        cluster_2.append(point)

center_1 = calc_centers(cluster_1)
center_2 = calc_centers(cluster_2)

min_dist = 10**10
for p in cluster_2:
    color = p[2][0]
    size = p[2][2:]
    if color == 'Y' and size == 'III':
        d = dist(p[:2], center_2[:2])
        if d < min_dist:
            min_dist = d

print(min_dist * 10000)

max_dist = -10**10
for p in cluster_1:
    color = p[2][0]
    size = p[2][2:]
    if color == 'Y' and size == 'III':
        d = dist(p[:2], center_2[:2])
        if d > max_dist:
            max_dist = d

print(max_dist * 10000)