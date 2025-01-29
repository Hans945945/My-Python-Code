import sys
place, d, speed_limit = map(int, input().split())
n = int(sys.stdin.readline())
for s in sys.stdin:
    ball, speed = map(int, s.split())
    range_l, range_r = place - d, place + d
    if ball >= range_l and ball <= range_r:
        if speed <= speed_limit:
            place = ball
        elif ball >= place:
            place -= 15
        else:
            place += 15
print(place)
            
