import sys
r = []
for s in sys.stdin:
    n,m = map(int, s.split())
    r.append(n*(n+1)*m*(m+1)//4)
sys.stdout.write("\n".join(map(str, r))+"\n")
