total = 0
for _ in range(5):
    n,m = map(int, input().split())
    if m > 0:
        total += n%m
print(total)
