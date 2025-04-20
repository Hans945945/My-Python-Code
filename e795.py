import sys
def is_prime(n):
    if n == 2:
        return 1
    if n < 2 or n % 2 == 0:
        return 0
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return 0
    return 1
r = []
for s in sys.stdin.readlines()[1:]:
    n = s.strip()
    flag = 1
    while n:
        if not is_prime(int(n)):
            flag = 0
            break
        n = n[1:]
    r.append(f"{s.strip()} is a Prime Day!" if flag else f"{s.strip()} isn't a Prime Day!")
sys.stdout.write("\n".join(r)+"\n")
