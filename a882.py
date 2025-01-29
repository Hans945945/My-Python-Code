import sys
data = sys.stdin.read().splitlines()
data.pop(0)
r = []
for l in data:
    r.append(str(l.count("X")*2+l.count("H")))
sys.stdout.write("\n".join(r)+"\n")
