from collections import Counter

N = int(input())
count = {}

spf = list(range(N + 1))
for i in range(2, int(N ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i

for i in range(2, N + 1):
    x = i
    while x > 1:
        p = spf[x]
        count[p] = count.get(p, 0) + 1
        x //= p
        
nums = Counter(count.values())

for k, v in sorted(nums.items(), reverse=True):
    if v == 1:
        print(k, end=" ")
    else:
        print(f"{v}*{k}", end=" ")
