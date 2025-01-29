Type = input().lower()
nums = list(map(int, list(input())))
r = nums.copy()
for t in set(Type):
    total = 0
    count = 0
    index = [i for i in range(len(nums)) if Type[i] == t]
    total = sum(nums[i] for i in index)
    for i in index:
        r[i] = total//len(index)
    index = index[::-1]
    for i in index[:total%len(index)]:
        r[i] += 1
print("".join(map(str, r)))
        
