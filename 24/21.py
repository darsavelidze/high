s = open('24_21.txt').readline()

cur_len = 1
max_len = -1


for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 1


print(max_len)
