import sys
def all_positive(nums):
    for i in nums:
        for j in i:
            if j < 0:
                return False
    return True
data = sys.stdin.read().splitlines()
T = int(data[0])
index = 1
for k in range(1, T+1):
    N = int(data[index].split()[2])
    index += 1
    nums = [0 for _ in range(N)]
    for i in range(N):
        nums[i] = list(map(int, data[index].split()))
        index+=1
    r = [row[::-1] for row in nums[::-1]]
    print(f"Test #{k}: Symmetric." if nums == r and all_positive(nums) else f"Test #{k}: Non-symmetric.")
