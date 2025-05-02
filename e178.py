import sys
data = sys.stdin.read().splitlines()

i = 0
r = []
while i < len(data):
    n, k = map(int, data[i].split())
    i += 1
    if n == 0:
        r.append("0")
        continue
    nums = list(map(int, data[i].split()))
    i += 1

    nums.sort() 

    for j in range(n):
        if k > 0 and nums[j] < 0:
            nums[j] = -nums[j]
            k -= 1
        else:
            break

    r.append(str(sum(nums)) if k % 2 == 0 else str(sum(nums)-min(nums)*2))

sys.stdout.write("\n".join(r) + "\n")
