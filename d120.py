import sys
def count_prime_factors(n):
    factor = 2
    factors = set()
    while factor * factor <= n:
        while n % factor == 0:
            factors.add(factor)
            n //= factor
        factor += 1
    if n > 1:
        factors.add(factor)
    return len(factors)
r = []
data = sys.stdin.read().splitlines()
for s in data[:-1]:
    n = int(s.strip())
    r.append(f"{n} : {count_prime_factors(n)}")
sys.stdout.write("\n".join(r)+"\n")
