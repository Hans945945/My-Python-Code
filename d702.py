import sys
n = 1000
dp = [0] * (n + 1)
dp[1] = dp[2] = dp[3] = 1

for i in range(4, n + 1):
    dp[i] = dp[i-2] + dp[i-3]

sys.stdout.write("\n".join(str(dp[int(s)]) for s in sys.stdin.read().split())+"\n")
