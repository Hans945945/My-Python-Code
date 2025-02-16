import sys
data = sys.stdin.readlines()
idx = 0
r = []
while idx < len(data):
    n = int(data[idx])
    ws = []
    vs = []
    for s in data[idx+1:idx + n+1]:
        a,b = map(int, s.split())
        ws.append(a)
        vs.append(b)

    dp = [0] * 101

    for i in range(n):
        for j in range(100,ws[i]-1,-1):
            dp[j] = max(dp[j], dp[j-ws[i]] + vs[i])

    idx += n+1

    r.append(dp[-1])
sys.stdout.write("\n".join(map(str, r))+"\n")
