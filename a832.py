n = int(input())
a = list(range(1, n + 1))

for k in range(1, n+1):
    n = len(a)
    r = []
    for i in range(0, n, k):
        seg = a[i:i + k]
        if len(seg) > 1:
            r.extend(seg[1:] + [seg[0]])
        else:
            r.extend(seg)
    a = r

print(' '.join(map(str, a)))
