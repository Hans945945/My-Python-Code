import random
import sys
seen = set()
i = 100
r = []
while i > 0:
    a = random.randint(1,1000000)
    b = random.randint(1,1000000)
    c = a+b
    if c not in seen:
        r.append(f"{a} {b} {c}")
        seen.add(c)
        i -= 1
sys.stdout.write("\n".join(r)+"\n")
