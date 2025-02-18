import sys
seen = set()
r = []
for s in sys.stdin.readlines():
    q,t = s.split()
    if t == "0" and q not in seen:
        seen.add(q)
        r.append(q)
sys.stdout.write("\n".join(r)+"\n")
