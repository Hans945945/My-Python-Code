import sys
from itertools import groupby
nums = [0 for _ in range(31)]
nums[0] = "1"
for i in range(1, 31):
    '''
    r=[]
    count = 1
    for i in range(1, len(nums[j-1])):
        if nums[j-1][i] != nums[j-1][i-1]:
            r.append(count)
            r.append(nums[j-1][i-1])
            count = 0
        count += 1
    if count > 0:
        r.append(count)
        r.append(nums[j-1][-1])
    '''
    nums[i] = "".join(f"{len(list(group))}{char}" for char, group in groupby(nums[i-1]))
sys.stdout.write("\n".join(nums[int(s)] for s in sys.stdin.read().splitlines())+"\n")
