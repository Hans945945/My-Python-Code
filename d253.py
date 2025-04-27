import sys
r = []
dp = [0]*7490
dp[0] = 1
for n in [1,5,10,25,50]:
    for i in range(n,7490):
        dp[i] += dp[i-n]
sys.stdout.write("\n".join(str(dp[int(s)]) for s in sys.stdin.readlines())+"\n")
