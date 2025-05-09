import sys
for s in sys.stdin.readlines()[1:]:
    a,b = s.split()
    n = max(len(a),len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    count = 0
    flag = 0
    for i in range(n-1, -1, -1):
        now = int(a[i]) + int(b[i])  + flag
        if now >= 10:
            flag = 1
            count += 1
        else:
            flag = 0
    print(count)
