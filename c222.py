import sys
r = []
for s in sys.stdin:
    a,b = map(int, s.split())
    r.append(a^b)
sys.stdout.write("\n".join(map(str, r))+"\n")
