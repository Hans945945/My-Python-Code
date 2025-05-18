import sys
for s in sys.stdin.readlines()[:-1]:
    a = int(s)
    r = []
    for k in range(1,10):
        if (a - k) % 9 == 0:
            r.append(str(10*(a-k)//9+k))
    if a % 9 == 0:
        r.append(str(10*a//9))
    print(" ".join(r))    
