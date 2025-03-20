import sys
r = []
for s in sys.stdin.readlines():
    nums = s.split()[1:]
    r.append("".join(sorted(nums, key = lambda x:x*10, reverse = True)))
sys.stdout.write("\n".join(r)+"\n")
