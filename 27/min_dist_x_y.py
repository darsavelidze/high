from math import dist

points = [[1, 2], [5, 7], [20, 30], [10, 6]]

min_sum = 10**10
p = None

for a in points:
    cur_sum = 0
    for b in points:
        cur_sum += dist(a, b)

    if cur_sum < min_sum:
        min_sum = cur_sum
        p = a

print(p, min_sum)
