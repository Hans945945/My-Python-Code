import sys
def GCD(a,b):
    while b:
        a,b = b,a%b
    return a
r = []
for s in sys.stdin.readlines():
    h,k,x,y = map(int, s.split())
    d = abs(x-h)
    a = (y-k)*d//(x-h)**2
    b = h*-2*a
    c = h**2*a+k*d
    e = GCD(GCD(a,b),GCD(c,d))
    r.append(f"{d//e}y = {a//e}x^2 + {b//e}x + {c//e}")
sys.stdout.write("\n".join(r)+"\n")
