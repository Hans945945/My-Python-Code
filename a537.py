import sys
from collections import Counter
isPrime = [1]*2001
isPrime[0] = isPrime[1] = 0
for i in range(2, int(2000**0.5)+1):
    if isPrime[i]:
        for j in range(i*i, 2001, i):
            isPrime[j] = 0
data = sys.stdin.read().splitlines()
T = data[0]
for i in range(1,len(data)):
    r = [key for key, value in Counter(data[i]).items() if isPrime[value]]
    sys.stdout.write(f"Case {i}: {''.join(sorted(r))}\n" if r else f"Case {i}: empty\n")
