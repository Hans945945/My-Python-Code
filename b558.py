import sys

nums = []
start = 1
num = 0
for i in range(500):
    start = start + num
    nums. append(start)
    num = num + 1

for s in sys.stdin:
    print(nums[int(s)-1])
    
