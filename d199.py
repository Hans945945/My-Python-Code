import sys
r = []
for s in sys.stdin.readlines():
    a,b,c = map(int, s.split())
    r.append(int(((a+b+c)**2-4*a*c)**0.5))
sys.stdout.write("\n".join(map(str, r))+"\n")
