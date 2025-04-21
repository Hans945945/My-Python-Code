import sys
seen = {}
def count(n, p, r):
    if (n,p,r) in seen:
        return seen[(n,p,r)]
    if p <= 0 or r <= 0 or p+r > n+1:
        return 0
    
    if n == 1:
        return 1 if p == 1 and r == 1 else 0

    ans = (n - 2) * count(n - 1, p, r)
    ans += count(n - 1, p - 1, r)
    ans += count(n - 1, p, r - 1)

    seen[(n,p,r)] = ans
    return ans
result = []
for s in sys.stdin.readlines()[1:]:
    n,p,r = map(int, s.split())
    result.append(str(count(n,p,r)))
sys.stdout.write("\n".join(result)+"\n")
