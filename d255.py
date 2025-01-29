import sys
def GCD(a, b):
    while b:
        a,b = b, a%b
    return a
table = [[GCD(i,j) for j in range(1,501)] for i in range(1,501)]
r = []
for s in sys.stdin:
    n = int(s)
    if n == 0:
        break
    total = 0
    
    r.append(str(sum([sum(table[i][i+1:n]) for i in range(n-1)])))
sys.stdout.write("\n".join(r))
