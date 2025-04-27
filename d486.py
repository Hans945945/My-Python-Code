import sys
r = []
for s in sys.stdin.readlines()[:-1]:
    n = int(s)

    r.append(f"f({n})")
    now = [n]

    while any(x >= 2 for x in now):
        next_now = []
        for x in now:
            if x >= 2:
                next_now.append(x - 1)
                next_now.append(x - 2)
            else:
                next_now.append(x)
        r.append(' '.join(f"f({x})" for x in next_now))
        now = next_now
    
    r.append(f"f({n}) = {len(now)}\n")
sys.stdout.write("\n".join(r))
