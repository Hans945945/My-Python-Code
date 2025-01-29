import sys
bricks = [1,1]
for i in range(2, 51):
    bricks.append(bricks[i-1]+bricks[i-2])
for s in sys.stdin:
    if s.strip() == "0":
        break
    print(bricks[int(s)])
