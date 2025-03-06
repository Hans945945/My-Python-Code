import sys
data = sys.stdin.readlines()
w,h = map(int, data.pop(0).split())
r = [f"{w} {h}"]
for i in range(h):
    nums = list(map(int, data[i].split()))
    now = []
    for j in range(0,w*3,3):
        temp = nums[j] + nums[j+1] + nums[j+2]
        temp = (temp+1) // 3
        now.append(f"{temp} {temp} {temp}")
    r.append(" ".join(now))
sys.stdout.write("\n".join(r)+"\n")
    
