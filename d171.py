import sys
import math
r = []
for s in sys.stdin.readlines():
    a,b = map(int, s.split())
    r.append(int(b*math.log10(a))+1)
sys.stdout.write("\n".join(map(str,r))+"\n")
