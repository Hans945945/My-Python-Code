import sys
r = []
data = sys.stdin.readlines()
for i in range(0,len(data),3):
    a = int(data[i])
    op = data[i+1].rstrip()
    b = int(data[i+2])
    if op == "*":
        r.append(str(a*b))
    else:
        r.append(str(a//b))
sys.stdout.write("\n".join(r)+"\n")
