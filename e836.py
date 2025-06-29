from collections import Counter
n = int(input())
temp = list(map(int, input().split()))
l = len(set(temp))
print(l)
if l == n:
    print("NO")
else:
    counter = Counter(temp)
    Max = max(counter.values())
    print(" ".join(str(k) for k,v in counter.items() if v == Max))
