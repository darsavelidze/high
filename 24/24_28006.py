f = open('24_28006.txt').readline()
a = set()
i = 0
nums = '0123456789'
# while i < len(f)-1:
#     if f[i] == '(' and f[i+1] in nums:
#
#     if f[i] == ')' and f[i+1] == '('
s = f.replace('(', 'h').replace(')', 'h')
s = s.split('h')
print(s)