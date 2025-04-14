import sys
r = []
for s in sys.stdin.readlines()[1:]:
    a,b = map(int, s.split())
    r.append(str(a-b))
sys.stdout.write("\n".join(r)+"\n")
