import sys
data = sys.stdin.readlines()[:-1]
r = []
for i in range(1,len(data),2):
    nums = data[i].split()
    r.append("".join(sorted(nums,key = lambda x:x*10, reverse = True)))
sys.stdout.write("\n".join(r)+"\n")
