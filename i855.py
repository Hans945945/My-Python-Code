import sys
data = sys.stdin.readlines()
T = int(data[0])
r = []
for i in range(1, 1+T*2, 2):
    n = int(data[i])
    nums = list(map(int, data[i+1].split()))
    count = 0
    for j in range(1,n):
        for k in range(j):
            if nums[j] >= nums[k]:
                count += 1
    r.append(count)
sys.stdout.write("\n".join(map(str, r))+"\n")
