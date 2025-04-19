from math import pi
import sys
r = []
for s in sys.stdin.readlines():
    a = float(s)
    center = a*a*(1+pi/3 - 3**0.5)
    dots = a*a*(-4+pi/3+2*3**0.5)
    r.append(f"{center:.3f} {dots:.3f} {a*a-center-dots:.3f}")
sys.stdout.write("\n".join(r)+"\n")
