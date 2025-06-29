import sys
for s in sys.stdin:
    a,b,c,d = map(int, s.split())
    print(a+c-b-d)

