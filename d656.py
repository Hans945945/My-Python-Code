import sys
r = []
case = 0
for s in sys.stdin.readlines()[:-1]:
    if s.rstrip() == "0":
        break
    case += 1
    r.append(f"Case {case}: {int(s)//2}")
sys.stdout.write("\n".join(r)+"\n")
