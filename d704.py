import sys
fib = [2,3,5,8,13,21,34,55,89]
r = []
for s in sys.stdin:
    temp = []
    n = int(s)
    i = 0
    while n > 0:
        temp.insert(0,n % fib[i])
        n //= fib[i]
        i += 1
    r.append(",".join(map(str, temp)))
sys.stdout.write("\n".join(r)+"\n")
