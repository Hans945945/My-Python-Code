import sys
from itertools import groupby

r = []
for s in sys.stdin.readlines():
    r.append("".join(f"{len(group)}{k}" if len(group) > 2 else "".join(group) for k, g in groupby(s.strip()) for group in [list(g)]))
sys.stdout.write("\n".join(r) + "\n")

    
