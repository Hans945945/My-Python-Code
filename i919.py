import sys
r = []
case = 0
for s in sys.stdin.readlines()[1:]:
    case += 1
    a,b,c = map(int, s.split())
    r.append(f"Case {case}: {'good' if a <= 20 and b <= 20 and c <= 20 else 'bad'}")
sys.stdout.write("\n".join(r)+"\n")
