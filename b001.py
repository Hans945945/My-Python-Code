import sys
for S in sys.stdin:
    parts = S.split()
    k = int(parts[0])
    s = parts[1]
    count = 0

    n = len(s)
    for i in range(n):
        for l in range(1, (n-i-k)//2 + 1):
            u1 = s[i:i+l]
            u2_start = i + l + k
            if u2_start + l <= n:
                u2 = s[u2_start:u2_start + l]
                if u1 == u2:
                    count += 1
                    
    print(count)

