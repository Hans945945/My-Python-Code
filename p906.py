n,a = map(int, input().split())
nums = list(map(int, input().split()))
b = int(nums.pop())
print(" ".join(str((n*b+a-1)//a) for n in nums))
