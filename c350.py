n,k,w = map(int, input().split())
total = n
while n >= k:
    total += w
    n += w
    n -= k
print(total)
