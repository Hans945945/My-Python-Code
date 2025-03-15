import sys
N = 671064
dp = [1]*(N+1)
dp[0] = dp[1] = 0
for i in range(2,int(N**0.5)+1):
    if dp[i]:
        for j in range(i*i,N+1,i):
            dp[j] = 0
r = []
for s in sys.stdin.readlines():
    r.append("It's a prime!!!" if dp[int(s)] else "It's not a prime!!!")
sys.stdout.write("\n".join(r)+"\n")
