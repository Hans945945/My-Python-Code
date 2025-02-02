import sys
result = []
for s in sys.stdin:
    if s.strip() == "-1":
        break
    nums = list(map(int, s.split()))
    r = [0 for _ in range(len(nums))]
    for i in range(len(nums)):
        now = nums[i]
        now += 1
        count = 0
        for j in range(len(nums)):
            if r[j] == 0:
                count += 1
                if count == now:
                    r[j] = i+1
                    break
    result.append(" ".join(map(str,r)))
sys.stdout.write("\n".join(result)+"\n")
