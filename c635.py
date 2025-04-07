import sys
r = []
for s in sys.stdin.readlines():
    nums = list(map(int, s.split(",")))

    odd = nums[::2]
    even = nums[1::2]

    odd.sort()
    even.sort()

    temp = []
    for i in range(len(nums)):
        if i % 2 == 0:
            temp.append(str(odd[i//2]))
        else:
            temp.append(str(even[i//2]))
    r.append(",".join(temp))
sys.stdout.write("\n".join(r)+"\n")
