import sys
from itertools import product
r = []
for s in sys.stdin:
    n = int(s)
    r.extend([''.join(bits) for bits in product("01", repeat = n)])
sys.stdout.write("\n".join(r)+"\n")
    
