from math import dist

def calc_centers(cluster):
    min_sum = 10 ** 10
    center = None
    for p_1 in cluster:
        cur_sum = 0
        for p_2 in cluster:
            cur_sum += dist(p_1, p_2)
        if cur_sum < min_sum:
            min_sum = cur_sum
            center = p_1
    return center


f = open('27B_27780.txt')

cluster_1 = []
cluster_2 = []
cluster_3 = []

for line in f:
    point = [float(x) for x in line.replace(',', '.').split()]
    if point[0] > 24:
        cluster_1.append(point)
    elif point[1] > 22:
        cluster_2.append(point)
    else:
        cluster_3.append(point)


center_1 = calc_centers(cluster_1)
center_2 = calc_centers(cluster_2)
center_3 = calc_centers(cluster_3)

print(len(cluster_1))
print(len(cluster_2))
print(len(cluster_3))

k = 0
for p in cluster_3:
    if dist(p, center_3) < 1.2 and p != center_3:
        k += 1
print(k)

min_dist = 10**10
for p in cluster_2:
    if dist(p, center_2) < min_dist and p != center_2:
        min_dist = dist(p, center_2)
print(min_dist * 10000)
