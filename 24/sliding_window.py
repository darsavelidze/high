s = '*aa**aa*'
left = 0
best = 0
count = 0

for right in range(len(s)):
    count = s[left:right + 1].count('*')

    while count > 2:
        left += 1
        count = s[left:right + 1].count('*')

    if count == 2:
        best = max(best, right - left + 1)
        print(left, right)

print(best)