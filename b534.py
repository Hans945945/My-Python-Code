import sys
def GCD(a,b):
    while b:
        a,b = b,a%b
    return a
N = 65536
table = [1]*(N+1)
table[0] = table[1] = 0
for i in range(2, int(N**0.5)+1):
    if table[i]:
        for j in range(i*i, N+1, i):
            table[j] = 0
r = []
for s in sys.stdin.readlines()[1:]:
    a,b = map(int, s.split())
    n = a
    i = 2
    temp = []
    while i*i <= n:
        count = 0
        while n%i == 0:
            n //= i
            count += 1
        if count == 1:
            temp.append(str(i))
        elif count > 1:
            temp.append(f"{i}^{count}")
        i += 1
    if n > 1:
        temp.append(str(n))
    g = GCD(a,b)
    r.append(' , '.join(["*".join(temp),str(g),"Y" if table[g] else "N"]))
sys.stdout.write("\n".join(r)+'\n')
        
