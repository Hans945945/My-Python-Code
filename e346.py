from itertools import accumulate
import sys
l = int(sys.stdin.readline())
nums = [0]+list(accumulate(map(int, sys.stdin.readline().split())))
q = sys.stdin.readline()
r = []
for s in sys.stdin:
    left, right = map(int, s.split())
    r.append(str(nums[right]-nums[left-1]))
sys.stdout.write("\n".join(r)+"\n")
