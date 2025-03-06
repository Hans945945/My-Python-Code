import sys
data = sys.stdin.readlines()
T = int(data[0])
w,h = map(int, data[1].split())
r = [f"{w} {h}"]
for i in range(2,h+2):
    nums = list(map(int, data[i].split()))
    now = []
    for j in range(0,w*3,3):
        if (nums[j] + nums[j+1] + nums[j+2])/3 >= T:
            now.append("255 255 255")
        else:
            now.append("0 0 0")
    r.append(" ".join(now))
sys.stdout.write("\n".join(r)+"\n")
