import sys
r = []
for s in sys.stdin.readlines()[:-1]:
    n,m = map(int, s.split())
    r.append(n**m)
sys.stdout.write("\n".join(map(str, r))+"\n")
