import sys
r = []
for s in sys.stdin.readlines():
    n = int(s)
    a = n//4
    b = n//2-a
    r.append(a*b)
sys.stdout.write("\n".join(map(str,r))+"\n")
