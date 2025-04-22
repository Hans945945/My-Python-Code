import sys
from datetime import date
data = sys.stdin.readlines()
r = []
for i in range(0,len(data), 2):
    y1, m1, d1 = map(int, data[i].split())
    y2, m2, d2 = map(int, data[i+1].split())
    r.append(str(abs((date(y1, m1, d1) - date(y2, m2, d2)).days)))
sys.stdout.write("\n".join(r)+"\n")
