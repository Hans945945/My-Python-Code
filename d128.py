import sys
r = []
for s in sys.stdin.readlines():
    a,b,c = map(int, s.split())
    r.append(max(a+b+c,a+b*c,a*b+c,a*b*c,a+b*10+c,a*10+b+c,a*(b*10+c), (a*10+b)*c))
sys.stdout.write("\n".join(map(str, r))+"\n")
