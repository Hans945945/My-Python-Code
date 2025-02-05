import sys

n = int(sys.stdin.readline())
Map = []
candidates = []

i = 0
for s in sys.stdin:
    row = list(map(int, s.split()))
    Map.append(row)

    ys = []
    max_y = float("-inf")
    for j, y in enumerate(row):
        if y > max_y:
            max_y = y
            ys = [j]
        elif y == max_y:
            ys.append(j)

    candidates.extend((i, y) for y in ys)
    i += 1

Map = list(zip(*Map))

out = False
for i, row in enumerate(Map):
    xs = []
    min_x = float("inf")

    for j, x in enumerate(row):
        if x < min_x:
            min_x = x
            xs = [j]
        elif x == min_x:
            xs.append(j)

    for x in xs:
        if (x, i) in candidates:
            print(x, i)
            out = True
            break
    if out:
        break

if not out:
    print("NO")
