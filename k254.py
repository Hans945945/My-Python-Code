s, e, b, k = map(int, input().split())
count = 0
flag = 0
for n in range(s, e + 1):
    if n % b == 0 or str(b) in str(n):
        count += 1
        if count == k:
            flag = 1
            break
print(n if flag else -1)
