import sys
primes = {2, 3, 5, 7, 11, 13, 17, 19}

def is_prime(n, primes_set):
    if n <= 1:
        return False
    if n in primes_set:
        return True
    if any(n % p == 0 for p in primes_set):
        return False
    for p in range(5, int(n ** 0.5) + 1, 6):
        if n % p == 0 or n % (p + 2) == 0:
            return False
    primes_set.add(n)
    return True

result = []
for s in sys.stdin.readlines():
    nums = s.strip()
    l = 0
    r = 1
    temp = []
    for r in range(1,11):
        n = int(nums[l:r])
        if is_prime(n, primes):
            temp.append(n)
            l = r
    result.append(len(temp))
    result.extend(temp)
    result.append("")
sys.stdout.write("\n".join(map(str, result))+"\n")
