x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())
px,py = map(int, input().split())
if min(x1,x2) < px < max(x1,x2) and min(y1,y2) < py < max(y1,y2):
    if min(x3,x4) < px < max(x3,x4) and min(y3,y4) < py < max(y3,y4):
        print(0)
    else:
        print(1)
else:
    print(2)
    
