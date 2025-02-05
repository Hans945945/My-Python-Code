from itertools import groupby 
data = sorted(input()) 
nums = [(key, len(list(group))) for key, group in groupby(data)]
nums.sort(key=lambda x: (-x[1], x[0]))
print(" ".join(key for key, _ in nums))
