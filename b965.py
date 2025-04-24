r,c,m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(r)]
op = input().split()[::-1]
for o in op:
    if o == "1":
        nums = nums[::-1]
    else:
        nums = [list(row) for row in zip(*nums)][::-1]
print(len(nums),len(nums[0]))
for n in nums:
    print(" ".join(map(str, n)))
    
