n = int(input())
t = int(input())
rocks = []
for _ in range(t):
    w, p = map(int, input().split())
    rocks.append((p, w))
rocks.sort(reverse = True)
total = 0
for p, w in rocks:
    if w > n:
        total += p*n
        break
    total += p*w
    n-=w
print(total)
