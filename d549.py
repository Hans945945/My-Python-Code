import sys
r = []
for s in sys.stdin.readlines():
    a,b,c = map(int,s.split())
    r.append(f"{(a*a+c*c-b*b)**0.5:.2f}")
sys.stdout.write("\n".join(r)+"\n")
