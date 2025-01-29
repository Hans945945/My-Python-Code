import sys
from itertools import accumulate
import operator
N = 48611
isPrime = [1]*(N+1)
isPrime[0] = isPrime[1] = 0
        
for i in range(2,int(N**0.5)+1):
    if isPrime[i]:
        for j in range(i**2, N+1, i):
            isPrime[j] = 0
prime_m = list(accumulate([i for i in range(N+1) if isPrime[i]], operator.mul))

for s in sys.stdin:
    print(prime_m[int(s)-1])
