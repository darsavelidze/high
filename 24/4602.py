s = open('24_4602.txt').readline()

cur_len = 0
max_len = -1

i = 1
while i < len(s):
    if s[i - 1] in 'BCD' and s[i] in 'AOAOAOAOAOAO':
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
        i += 2
    else:
        cur_len = 0
        i += 1

print(max_len)
