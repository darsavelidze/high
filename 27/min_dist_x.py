points = [1, 5, 7, 9, 20]

min_sum = 10000000
p = -1
for a in points:
    cur_sum = 0
    for b in points:
        cur_sum += abs(a - b)
    if cur_sum < min_sum:
        min_sum = cur_sum
        p = a

print(min_sum, p)