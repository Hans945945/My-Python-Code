import sys
input()
case = 1
for s in sys.stdin:
    n = int(s)
    r = n*(n-1)/4
    if r != int(r):
        r = f"{int(r*2)}/2"
    else:
        r = int(r)
    print(f"Case {case}: {r}")
    case+=1
