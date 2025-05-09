import sys
for s in sys.stdin.readlines()[1:]:
    x,y,z = map(int, s.split())
    diff = y-z
    x -= y
    if x <= 0:
        print(1)
    elif diff <= 0:
        print("Poor Snail")
    else:
        print(x//diff+(x%diff!=0)+1)
