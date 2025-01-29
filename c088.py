from collections import defaultdict
N = 32767
isPrime = [1]*(N+1)
isPrime[0] = 0
isPrime[1] = 0
prime = []
for i in range(2,int(N**0.5)+1):
    if isPrime[i]:
        prime.append(i)
        for j in range(i*i, N+1, i):
            isPrime[j] = 0
#prime = [i for i in range(2, N+1) if isPrime[i]]
while True:
    nums = list(map(int, input().split()))
    if nums [0] == 0:
        break
    n = 1
    for i in range(0, len(nums), 2):
        n *= nums[i]**nums[i+1]
    n -= 1
    factors = defaultdict(int)
    
    for p in prime:
        if p*p > n:
            break
        while n % p == 0:
            factors[p] += 1
            n //= p
        if n == 1:
            break

    if n > 1:
        factors[n] += 1
        
    r = []
    for Prime, e in sorted(factors.items(), reverse = True):
        r.append(f"{Prime} {e}")
    print(" ".join(r))
        
            
    
    
    
