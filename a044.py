import sys
r = []
for s in sys.stdin.readlines():
    n = int(s)
    r.append(f"{(n**3+5*n+6)//6}")
sys.stdout.write("\n".join(r)+"\n")
