import sys
N = 1000000
isPrime = [1]*(N+1)
isPrime[0] = isPrime[1] = 0
        
for i in range(2,int(N**0.5)+1):
    if isPrime[i]:
        for j in range(i**2, N+1, i):
            isPrime[j] = 0
            
for s in sys.stdin:
    if s.strip() == "0":
        break
    print(0 if isPrime[int(s)] else 1)
