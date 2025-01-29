import sys
for s in sys.stdin:
    o, n = s.split()
    n = "".join([t for t in n if t in o])
    print("Yes" if o in n else "No")
