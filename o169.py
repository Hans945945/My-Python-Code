import sys
r = []
for s in sys.stdin:
    n,a = map(int, s.split())
    total = 0
    for i in range(1,n+1):
        total += i*a**i
    r.append(total)
sys.stdout.write("\n".join(map(str,r))+"\n")
