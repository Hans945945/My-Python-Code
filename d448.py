import sys
r = []
for s in sys.stdin:
    t1, t2, t3, x1, x3 = map(float, s.strip().split())
    r.append(f"{x3+(t2-t3)*((x1-x3)/(t1-t3)):.6f}")
sys.stdout.write("\n".join(r)+"\n")
