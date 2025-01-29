import sys
dp = [[0,0] for _ in range(51)]
dp[0][1] = 1
dp[1][0] = 1
dp[1][1] = 1
for i in range(2,51):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
total = [str(m+f) for m,f in dp]
r = []
for s in sys.stdin:
    n = int(s)
    if n == -1:
        break
    r.append(f"{str(dp[n][0])} {total[n]}")
sys.stdout.write("\n".join(r)+"\n")
