import sys
data = sys.stdin.readlines()
N = int(data.pop(0))
idx = 0
r = []
for i in range(N):
    money = 0
    for _ in range(12):
        money += float(data[idx])
        idx += 1
    r.append(f"{i+1} ${money / 12:,.2f}")
sys.stdout.write("\n".join(r)+"\n")
    
