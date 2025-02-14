from fractions import Fraction
import sys
def K(n):
    if n == 1:
        return 1
    elif n > 1:
        return K(n-1)*2
    else:
        return K(1/n) + 1
r = []
for s in sys.stdin:
    a,b = map(int, s.split())
    r.append(K(Fraction(a,b)))
sys.stdout.write("\n".join(map(str, r))+"\n")
