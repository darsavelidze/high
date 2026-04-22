s = open('24_28943.txt').readline()

count_20 = 0
left = 0
min_len = 10 ** 10
for right in range(len(s) - 1):
    if s[right] + s[right + 1] == '20':
        count_20 += 1

    if s[right] in 'AEIOUY':
        if count_20 >= 26:
            while count_20 != 25:
                if s[left] + s[left + 1] == '20':
                    count_20 -= 1
                left += 1

            left -= 1
            min_len = min(min_len, right - left + 1)
        count_20 = 0
        left = right + 1

print(min_len)
