ns = list(map(int, input().split()))
ms = list(map(int, input().split()))
total = 0
for i in range(5):
    n,m = ns[i],ms[i]
    if m > 0:
        total += n%m
print(total)
