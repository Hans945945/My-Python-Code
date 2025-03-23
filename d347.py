import sys
r = []
for s in sys.stdin.readlines():
    n = int(s)
    p = 1
    while p < n:
        p *= 18
    r.append("Stan wins." if n <= p // 2 else "Ollie wins.")
sys.stdout.write("\n".join(r)+"\n")
