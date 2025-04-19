import sys
r = ["INTERSECTING LINES OUTPUT"]
for s in sys.stdin.readlines()[1:]:
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, s.split())
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3

    det = dx1 * dy2 - dx2 * dy1

    if det == 0:
        if (y3 - y1) * dx1 == (x3 - x1) * dy1:
            r.append("LINE")
        else:
            r.append("NONE")
    else:
        t = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / det
        x = x1 + t * dx1
        y = y1 + t * dy1
        r.append(f"POINT {x:.2f} {y:.2f}")
r.append("END OF OUTPUT")
sys.stdout.write("\n".join(r)+"\n")
