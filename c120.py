import sys
import math
r = []
for s in sys.stdin.readlines():
    n = int(s)
    r.append(f"{n}!")
    r.append(f"{math.factorial(n)}")
sys.stdout.write("\n".join(r)+"\n")
    
