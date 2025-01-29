import sys
data = sys.stdin.read().splitlines()
index = 0
r = []
while index < len(data):
    n = int(data[index])
    index += 1
    nums = data[index].split()
    while len(nums) >= 1:
        r.append(" ".join(nums))
        nums.pop(0)
        nums = nums[::-1]
    r.append("")
    index += 1
sys.stdout.write("\n".join(r)+"\n")
