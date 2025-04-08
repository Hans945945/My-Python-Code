import sys
r = []
data = sys.stdin.readlines()
for k in range(0,len(data),2):
    a = data[k].rstrip()
    b = data[k+1].rstrip()
    n,m = len(a),len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    r.append(str(dp[n][m]))
sys.stdout.write("\n".join(r)+"\n")
