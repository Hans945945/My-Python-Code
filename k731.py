import sys
def change_d(d_now, d_to, left, right, turn):
    diff = (d_to - d_now)%360
    if diff == 90:
        right += 1
    elif diff == 270:
        left += 1
    elif diff == 180:
        turn += 1
    return left,right,turn
n = int(sys.stdin.readline())
x,y = map(int, sys.stdin.readline().split())
left = right = turn = 0
d = 90
for s in sys.stdin:
    x_now,y_now = map(int, s.split())
    if x_now == x:
        if y_now > y:
            d_to = 0
        else:
            d_to = 180
    else:
        if x_now > x:
            d_to = 90
        else:
            d_to = 270
    left,right,turn = change_d(d,d_to,left,right,turn)
    d = d_to
    x,y = x_now,y_now
print(left,right,turn)
