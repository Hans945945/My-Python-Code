import sys
r = []
data = sys.stdin.readlines()
for i in range(0,len(data),2):
    n = int(data[i])
    p = int(data[i+1])
    t = int(pow(p,1/n))
    r.append(t+1 if t**n != p else t)
sys.stdout.write("\n".join(map(str,r))+"\n")
