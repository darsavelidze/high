s = open('24_28943.txt').readline()

count_20 = 0
left = 0
min_len = float('inf')

for right in range(len(s)):
    if s[right] in 'AEIOUY':
        left = right - 1

        while count_20 < 26 and left > 0 and s[left] not in 'AEIOUY':
            if s[left - 1] + s[left] == '20':
                count_20 += 1
            left -= 1

        if count_20 == 26:
            min_len = min(min_len, right - left + 1)

        count_20 = 0

print(min_len)
