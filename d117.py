import sys
primes = {2,3,5,7,11,13,17,19}
def is_prime(n,primes):
    if n <= 0:
        return False
    if n in primes or n == 1:
        return True
    if any(n%p==0 for p in primes):
        return False
    for p in range(5,int(n**0.5)+1,6):
        if n%p == 0 or n%(p+2) == 0:
            return False
    return True

r = []
for s in sys.stdin.readlines():
    n = 0
    for w in s.strip():
        i = ord(w)
        if i>= 97:
            n += i-96
        else:
            n += 26+i-64
    r.append("It is a prime word." if is_prime(n,primes) else "It is not a prime word.")
sys.stdout.write("\n".join(r)+"\n")
