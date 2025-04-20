m,n,k = map(int, input().split())
count = m
while m >= n and count < k:
    count += m//n
    m = m//n + m%n
print("YES" if count >= k else "NO")

