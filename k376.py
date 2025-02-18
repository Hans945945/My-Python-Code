import sys
isPrime = [1]*5001
isPrime[0] = isPrime[1] = 0
prime = []
for i in range(2,5001):
    if isPrime[i]:
        prime.append(i)
        for j in range(i*i, 5001, i):
            isPrime[j] = 0
biggest_prime = float('-inf')
biggest = float('-inf')
for s in sys.stdin.readlines()[1:]:
    n = int(s)
    now = 1
    for p in prime:
        if p > n:
            break
        if n % p == 0:
            now = p
    if now > biggest_prime or (now == biggest_prime and n > biggest):
        biggest_prime = now
        biggest = n
print(biggest)
        
