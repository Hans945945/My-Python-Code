import sys
def isPrime(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0:
        return 0

    r,d = 0, n-1
    while d % 2 == 0:
        d //= 2
        r += 1
    bases = [2,7,61]

    def is_composite(a):
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            return 0
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                return 0
        return 1

    for b in bases:
        if b >= n:
            break
        if is_composite(b):
            return 0
    return 1
for s in sys.stdin:
    if s.strip() == "0":
        break
    print(0 if isPrime(int(s)) else 1)
