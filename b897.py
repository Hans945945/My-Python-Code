import sys, math
log = math.log10
r = []
for s in sys.stdin:
    n, k = map(int, s.split())
    if k == 0 or k == n:
        r.append("1")
        continue
    f = lambda x: 0.5 * log(2 * math.pi * x) + x * (log(x) - math.log10(math.e)) if x > 0 else 0
    r.append(str(int(f(n) - f(k) - f(n - k)) + 1))
print("\n".join(r))

