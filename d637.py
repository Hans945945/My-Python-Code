import sys
ws = []
vs = []
data = sys.stdin.readlines()
n = int(data[0])
for s in data[1:]:
    a,b = map(int, s.split())
    ws.append(a)
    vs.append(b)
dp = [0] * 101
for i in range(n):
    for j in range(100,ws[i]-1,-1):
        dp[j] = max(dp[j], dp[j-ws[i]] + vs[i])
print(dp[-1])
