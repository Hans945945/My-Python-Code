import sys
r = []
for s in sys.stdin.readlines()[1:]:
    r.append(sum(map(int, s.split(" + "))))
sys.stdout.write("\n".join(map(str, r))+"\n")
