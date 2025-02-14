import sys
from fractions import Fraction
r = []
for s in sys.stdin:
    a,b,c,d,o = s.split()
    a,b,c,d = map(int, [a,b,c,d])
    if o == "+":
        e = b*c + a*d
        f = b*d
    elif o == "-":
        e = a*d - b*c
        f = b*d
    elif o == "*":
        e = a*c
        f = b*d
    else:
        e = a*d
        f = b*c
    r.append(Fraction(e,f))
sys.stdout.write("\n".join(map(str, r))+"\n")
