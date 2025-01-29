import sys
for s in sys.stdin:
    print(s.rstrip() if int(s)%2 == 0 else int(s)-1)
