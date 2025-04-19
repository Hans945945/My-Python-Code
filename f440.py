import sys
data = sys.stdin.read().splitlines()
r = []
idx = 0
T = int(data[idx])
idx += 1

for _ in range(T):
    n = int(data[idx])
    idx += 1
    vs, ws = [], []
    for _ in range(n):
        v, w = map(int, data[idx].split())
        vs.append(v)
        ws.append(w)
        idx += 1

    dp = [0] * 31
    for i in range(n):
        for j in range(30, ws[i]-1, -1):
            dp[j] = max(dp[j], dp[j - ws[i]] + vs[i])

    g = int(data[idx])
    idx += 1
    total = 0
    for _ in range(g):
        mw = int(data[idx])
        total += dp[mw]
        idx += 1

    r.append(str(total))

sys.stdout.write("\n".join(r)+"\n")

        
