n = int(input())
nums = list(map(int, input().split()))
print(" ".join(map(str, [nums[0]]+[b-a for a,b in zip(nums[:-1], nums[1:])])))
