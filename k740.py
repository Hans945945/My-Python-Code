n = int(input())
nums = [[0 if i != 1 and i != j else 1 for i in range(1,j+1)] for j in range(1,n+1)]
for i in range(2, n):
    for j in range(1,i):
        nums[i][j] = nums[i-1][j] + nums[i-1][j-1]
nums = [" ".join(map(str, row)) for row in nums]
print("\n".join(nums))
