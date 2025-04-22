from collections import Counter
nums = list(map(int, input().split()))
print(max(Counter(nums).values()), end = " ")
print(*sorted(set(nums), reverse=True))
