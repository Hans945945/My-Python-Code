import sys
r = []
data = sys.stdin.readlines()
n,k,t = map(int, data.pop(0).split())
for i in range(n):
    now = list(map(int, data[i].split()))
    if (sum(now) - max(now) - min(now))/(k-2) >= t:
        r.append(str(i))
sys.stdout.write("\n".join(r)+"\n" if r else "A is for apple.\n")
