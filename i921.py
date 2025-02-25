import sys
r = []
case = 0
for s in sys.stdin.readlines()[1:]:
    case += 1
    c,d = map(int, s.split())
    r.append(f"Case {case}: {c + d*5/9:.2f}")
sys.stdout.write("\n".join(r)+"\n")
