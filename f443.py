import sys

n = int(sys.stdin.readline())
sales = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))

last = nums.index(-1)

while last != -1:
    if -1 in nums[last + 1:]:
        next_idx = nums.index(-1, last + 1)
    else:
        break
    current_range = sales[last + 1:next_idx]
    if current_range:
        max_idx = last + 1 + current_range.index(max(current_range))
        min_idx = last + 1 + current_range.index(min(current_range))

        nums[max_idx], nums[min_idx] = nums[min_idx], nums[max_idx]

    last = next_idx

sys.stdout.write(" ".join(map(str, nums)) + "\n")
