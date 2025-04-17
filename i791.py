from collections import Counter
n,k = map(int, input().split())
temp = Counter(input().split())
print(sum(v//k for v in temp.values()))
