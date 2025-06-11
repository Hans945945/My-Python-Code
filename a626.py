import sys
from bisect import bisect_right as right
N = 1000
dp = [1]*(N+1)
dp[0] = dp[1] = 0
primes = []
for i in range(2,int(N**0.5)+1):
    if dp[i] == 1:
        primes.append(i)
        for j in range(i*i,N+1,i):
            dp[j] = 0
primes = [i for i in range(2, N + 1) if dp[i]]

for s in sys.stdin.readlines():
    n = int(s)
    temp = primes[:right(primes,n)]
    for i in range(len(temp)):
        if i % 5 == 4:
            print(f"{temp[i]:>10}")
        else:
            print(f"{temp[i]:>10}", end = "")
    if len(temp) % 5 != 0:
        print()
