import sys
r = []
for s in sys.stdin.readlines()[1:]:
    a,b = s.split("-")
    a = sum((ord(a[i]) - 65)*26**(2-i) for i in range(3))
    r.append("nice" if abs(int(b)-a) <= 100 else "not nice")
sys.stdout.write("\n".join(r)+"\n")
