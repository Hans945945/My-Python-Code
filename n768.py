import sys
r = []
for s in sys.stdin.readlines()[1:]:
    nums = list(map(int, s.split()))
    N = nums.pop(0)
    avg = sum(nums)/N
    count = 0
    for n in nums:
        if n > avg:
            count += 1
    r.append(f"{count/N*100:.3f}%")
sys.stdout.write("\n".join(r)+"\n")
