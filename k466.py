import sys
n,m = map(int, sys.stdin.readline().split())
max_improve = max_regress = improve_idx = regress_idx = float("-inf")
i = 0
for s in sys.stdin:
    i+=1
    nums = list(map(int, s.split()))
    improve = 0
    regress = 0
    for j in range(1,m):
        d = nums[j] - nums[j-1]
        if d > 0:
            improve += d
        else:
            regress -= d
    if improve > max_improve:
        max_improve = improve
        improve_idx = i
    if regress > max_regress:
        max_regress = regress
        regress_idx = i
print(improve_idx,regress_idx,sep = "\n")
