import sys
import math
r = []
for s in sys.stdin:
    n = int(s)
    r.append(f"{n} -> {str(math.factorial(n)).rstrip('0')[-1]}")
sys.stdout.write("\n".join(r)+"\n")
    
