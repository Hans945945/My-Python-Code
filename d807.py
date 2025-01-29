import sys
def GCD(a, b):
    while b:
        a,b = b, a%b
    return a
for s in sts.stdin:
    a,b = map(int, s.split())
    print(GCD(a,b))
