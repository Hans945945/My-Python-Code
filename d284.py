import sys
import math

def comb(n,k):
    return math.factorial(n)//(math.factorial(n-k)*math.factorial(k))

r = []
for s in sys.stdin.readlines()[:-1]:
    n = int(s)
    total = 0
    for z in range(0, n+1, 2):
        total += comb(n, z) * (9 ** (n-z))
    r.append(str(total))
sys.stdout.write("\n".join(r)+"\n")
