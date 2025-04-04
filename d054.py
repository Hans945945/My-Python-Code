import sys

r = []

dp = [0]*41
dp[1] = 1
dp[2] = 5
dp[3] = 11
for i in range(4,41):
    dp[i] = dp[i-1] + 4*dp[i-2] + 2*dp[i-3]

for s in sys.stdin.readlines()[1:]:
    n = int(s)
    r.append(str(dp[n]))

sys.stdout.write("\n".join(r) + "\n")
