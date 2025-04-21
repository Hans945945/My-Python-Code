import sys
dp = [0]*801
dp[0] = 1
dp[1] = 0
for i in range(2,801):
    dp[i] = (i-1) * (dp[i-1] + dp[i-2])
sys.stdout.write("\n".join(str(dp[int(s)]) for s in sys.stdin.readlines()[:-1])+"\n")
