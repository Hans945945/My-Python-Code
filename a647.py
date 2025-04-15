import sys
r = []
for s in sys.stdin.readlines()[1:]:
    m,p = map(int, s.split())
    x = p/m*100-100
    if x>=0:
        x+=0.000001
    else:
        x-=0.000001
    r.append(f"{x:.2f}% dispose" if x>=10 or x <= -7 else f"{x:.2f}% keep")
sys.stdout.write("\n".join(r)+"\n")
