divs = [2, 3, 5, 7]
pointer = 0

nums = [1, 1, 1, 4, 6, 10, 14, 4, 1, 1]

cur_len = 0
max_len = 0
for x in nums:
    if x % divs[pointer % len(divs)] == 0:
        cur_len += 1
        pointer += 1
    else:
        pointer = 0
        max_len = max(max_len, cur_len)
