import sys
n = int(sys.stdin.readline())
dots = []
for s in sys.stdin:
    x,y = map(int,s.split())
    dots.append((x,y))
max_len = d1 = d2 = 0
for i in range(n):
    for j in range(i+1,n):
        x1,y1 = dots[i]
        x2,y2 = dots[j]
        len_now = abs(x1-x2)**2 + abs(y1-y2)**2
        if len_now > max_len:
            max_len = len_now
            d1,d2 = i,j
print(d1,d2)
