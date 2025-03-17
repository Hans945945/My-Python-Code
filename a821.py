import sys
from collections import defaultdict
data = sys.stdin.readlines()
n,r = map(int, data[0].split())
win = defaultdict(int)
for s in data[1:]:
    w,l = s.split()
    win[w] += 1
    win[l] -= 0.5
print(max(win, key = win.get))
