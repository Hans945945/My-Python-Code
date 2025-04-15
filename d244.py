from collections import Counter
temp = Counter(input().split())
ans = 0
for k,n in temp.items():
    if n == 2:
        ans = k
        break
print(ans)
