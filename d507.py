a,b,c = sorted((map(int, input().split())))
if a**2 + b**2 > c**2:
    print("acute triangle")
elif a**2 + b**2 == c**2:
    print("right triangle")
else:
    print("obtuse triangle")
