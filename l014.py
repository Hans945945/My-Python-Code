import sys
data = sys.stdin.readlines()
x,y = map(int, data[0].split())
total = x*y
new = []
for s in data[1:]:
    now = s.strip()
    total -= now.count("-")
    new.append(now)
new = "".join(new)
r = []
for i in range(1,total+1):
    now = new.index(str(i))
    r.append(f"第{i}步為第{now // y + 1}列，第{now % y + 1}行")
sys.stdout.write("\n".join(r)+"\n")
