import sys
def GCD(a,b):
    while b:
        a,b = b,a%b
    return a
fib = [0]*10001
fib[0] = fib[1] = 1
for i in range(2,10001):
    fib[i] = fib[i-1] + fib[i-2]
    
r = []
for s in sys.stdin.readlines():
    m,n = map(int, s.split())
    r.append(str(fib[GCD(m,n)-1]))
sys.stdout.write("\n".join(r)+"\n")
