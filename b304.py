import sys
data = sys.stdin.readlines()[1:]
r = []
for s in data:
    for _ in range(64):
        s = s.strip().replace("[]","").replace("()","")
        if not s:
            break
    r.append("No" if s else "Yes")
sys.stdout.write("\n".join(r)+"\n")
