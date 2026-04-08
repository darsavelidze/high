s = open('24_1866.txt').readline()

max_len = -1
cur_len = 1
for i in range(1, len(s)):
    pair = s[i - 1] + s[i]
    if pair == 'ad' or pair == 'da':
        cur_len = 1
    else:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len

print(max_len)
