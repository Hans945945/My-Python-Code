import sys
data = sys.stdin.readlines()
T = int(data.pop(0))
idx = 0
r = []
for case in range(1,T+1):
    r.append(f"Case {case}:")
    n = int(data[idx])
    for _ in range(n):
        idx += 1
        r.append(" ".join(data[idx].split()))
    idx += 1
sys.stdout.write("\n".join(r)+"\n")
    
        
