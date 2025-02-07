import sys
dp = [0 for _ in range(10001)]
dp[0] = dp[1] = 1
for i in range(2,10001):
    dp[i] = (dp[i-1] + dp[i-2])%2012
r = []
for s in sys.stdin:
    r.append(dp[int(s)])
sys.stdout.write("\n".join(map(str, r))+"\n")
