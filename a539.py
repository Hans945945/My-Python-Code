import sys
data = sys.stdin.readlines()
idx = 0
r = []
while idx < len(data):
    n = int(data[idx])
    idx += 1
    nums = list(map(int, data[idx].split()))
    idx += 1
    count = 0
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
                count += 1
    r.append(f"Minimum exchange operations : {count}")
sys.stdout.write("\n".join(r)+"\n")

    
    
