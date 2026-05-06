f = open('26_9793.txt')
N = int(f.readline())
data = [list(map(int, x.split())) for x in f]

handled = []

for n, detail in enumerate(data, 1):
    shl, ocr = detail
    if shl < ocr:
        handled.append([shl, "shl", n])
    else:
        handled.append([ocr, "ocr", n])

handled = sorted(handled, key=lambda x: (x[0], x[1]))

print(handled[-1][-1])
print(len([x for x in handled if x[1] == 'shl']) - 1)
