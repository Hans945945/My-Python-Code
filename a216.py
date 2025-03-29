import sys
r = []
for s in sys.stdin.readlines():
    n = int(s)
    r.append(f"{n*(n+1)//2} {n*(n+1)*(n+2)//6}")
sys.stdout.write("\n".join(r)+"\n")
