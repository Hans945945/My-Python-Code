n,d = map(int, input().split())
b = []
for _ in range(n):
    p = list(map(int, input().split()))
    if max(p)-min(p) >= d:
        b.append(sum(p)//3)
print(len(b), sum(b))
