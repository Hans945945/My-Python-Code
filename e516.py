n = int(input())
while n != 0:
    top = 1
    north = 2
    west = 3
    for _ in range(n):
        d = input()
        if d == "north":
            temp = 7 - north
            north = top
            top = temp
        elif d == "south":
            temp = 7 - top
            top = north
            north = temp
        elif d == "west":
            temp = 7 - west
            west = top
            top = temp
        elif d == "east":
            temp = 7 -top
            top = west
            west = temp
    print(top)
    n = int(input())
