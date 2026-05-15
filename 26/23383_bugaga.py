f = open('26_23383.txt')
N = int(f.readline())
f = [list(map(int, x.split())) for x in f]
f = sorted(f, key=lambda x: (x[1], x[0]))
f.append([-1, -1])
nums = set()

for i in range(len(f) - 1):
    num, point = f[i]
    next_point = f[i + 1][1]
    nums.add(num)

    if next_point != point:
        max_len = float('-inf')
        cur_len = 1
        nums_list = sorted(nums)

        for j in range(1, len(nums_list)):
            if nums_list[j] - nums_list[j - 1] == 1:
                cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len
            else:
                cur_len = 1

        if max_len != float('-inf'):
            print(point, max_len)
            break

        nums = set()
