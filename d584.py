import sys
input = sys.stdin.read
for line in input().splitlines():
    c, level = map(int, line.split())
    if c == 0:
        print(0)
        continue
    point = 1
    point += (level-8)*3 if c == 2 else (level-10)*3

    point += 5 if level >= 120 else 2 if level >= 70 else 1 if level >= 30 else 0

    print(point)
