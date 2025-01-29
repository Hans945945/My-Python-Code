N = int(input())
M = int(input())
isPrime = [1]*(M+1)
isPrime[0] = isPrime[1] = 0
prime = []
for i in range(2,M+1):
    if isPrime[i]:
        prime.append(i)
        for j in range(i**2, M+1, i):
            isPrime[j] = 0
prime = [p for p in prime if p >= N]
print(len(prime))
print(sum(prime))
