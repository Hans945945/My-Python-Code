import sys
r = []
for s in sys.stdin.readlines():
    n = int(s)
    total = 0
    i = 2
    while i*i <= n:
        while n%i == 0:
            total += i
            n//=i
        i += 1
    if n > 1:
        total += n
    r.append(total)
sys.stdout.write("\n".join(map(str, r))+'\n')
