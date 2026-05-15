f = open('26_2_23175.txt')
N, M = map(int, f.readline().split())
weights = [int(f.readline()) for i in range(N)]
boxes = [int(f.readline()) for j in range(M)]

weights = sorted(weights)
boxes = sorted(boxes)

packed = []

while len(weights) > 0 and len(boxes) > 0:
    if weights[0] <= boxes[0]:
        packed.append([weights.pop(0), boxes.pop(0)])
    else:
        boxes.pop(0)

max_box = packed[-1][-1]
max_weight = max([x for x in weights if x <= max_box])
print(len(packed), max_weight - packed[-2][0])
