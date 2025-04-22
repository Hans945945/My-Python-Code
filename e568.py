import sys
data = sys.stdin.readlines()
n = int(data.pop(0))
r = []
for i in range(0,n*2,2):
    x1, y1, x2, y2 = map(int, data[i].split())
    x3, y3, x4, y4 = map(int, data[i+1].split())

    area1 = (x2 - x1) * (y2 - y1)
    area2 = (x4 - x3) * (y4 - y3)

    strong = max(0, min(x2, x4) - max(x1, x3)) * max(0, min(y2, y4) - max(y1, y3))

    weak = area1 + area2 - 2 * strong
    unsafe = 10000 - strong - weak

    r.append(f"Night {i//2+1}: {strong} {weak} {unsafe}")

sys.stdout.write("\n".join(r)+"\n")
