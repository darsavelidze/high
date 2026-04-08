s = open('24_4627.txt').readline()

cur_len = 0
max_len = -1

i = 2
while i < len(s):
    word = s[i - 2] + s[i - 1] + s[i]
    if word == 'NPO' or word == 'PNO':
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
        i += 3
    else:
        cur_len = 0
        i += 1

print(max_len)
