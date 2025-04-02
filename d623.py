import sys
r = []
data = sys.stdin.readlines()[:-1]
idx = 0
while idx < len(data):
    a,b = map(int,data[idx].split())
    idx += 1
    c,d = map(int,data[idx].split())
    idx += 1
    e = a*d-b*c
    if e == 0:
        r.append('cheat!')
    else:
        r.append(f"{d/e:.5f} {-b/e:.5f}")
        r.append(f"{-c/e:.5f} {a/e:.5f}")
sys.stdout.write("\n".join(r)+"\n")
