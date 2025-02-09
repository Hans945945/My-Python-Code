import sys

def comb(n, m):
    if m > n - m:
        m = n - m
    res = 1
    for i in range(m):
        res = res * (n - i) // (i + 1)
    return res

r = []
for s in sys.stdin.readlines()[:-1]:
    n,m = map(int,s.split())
    r.append(comb(n,m))
sys.stdout.write("\n".join(map(str, r))+"\n")
