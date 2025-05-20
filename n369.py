import sys
seen = set()
for s in sys.stdin.readlines()[1:]:
    a,b = s.split()
    if a in seen:
        print(b, "account has been used")
    else:
        print("welcome,", b)
        seen.add(a)
