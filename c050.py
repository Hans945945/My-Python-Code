import sys

MAX = 1000000

is_prime = [0,0] + [1] * (MAX - 2)
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX, i):
            is_prime[j] = 0

primes = [i for i in range(3, MAX, 2) if is_prime[i]]

for s in sys.stdin.readlines()[:-1]:
    n = int(s)

    found = 0
    ans = (0, 0)

    for a in primes:
        if a > n // 2:
            break
        b = n - a
        if is_prime[b]:
            ans = (a, b)
            found = 1
            break

    if found:
        a, b = ans
        print(f"{n} = {a} + {b}")
    else:
        print("Goldbach's conjecture is wrong.")
