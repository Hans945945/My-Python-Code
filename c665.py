import sys
result = []
for s in sys.stdin.readlines():
    n,b1,b2 = s.split()
    n = int(n,int(b1))
    q,r = divmod(n,int(b2))
    if r >= 10:
        r = chr(r-9+64)
    temp = [str(r)]
    while q:
        q,r = divmod(q,int(b2))
        if r >= 10:
            r = chr(r-9+64)
        temp.insert(0, str(r))
    result.append("".join(temp))
sys.stdout.write("\n".join(result)+"\n")
