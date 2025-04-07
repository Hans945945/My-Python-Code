import sys
r = []
data = sys.stdin.readlines()
T = int(data[0])
ans = list(data[1].strip())
for s in data[3:]:
    r.append(f"{100//T*sum(a == b for a,b in list(zip(ans, list(s.strip()))))}")
sys.stdout.write("\n".join(r)+"\n")
            
