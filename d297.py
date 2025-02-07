import sys
r = []
for s in sys.stdin:
    n = int(s)
    r.append((2*n**3+5*n**2+2*n -(n%2))//8)
sys.stdout.write("\n".join(map(str, r))+"\n")
