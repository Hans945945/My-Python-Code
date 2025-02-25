import sys
r = []
for s in sys.stdin.readlines()[1:]:
    a,b,c = sorted(map(int, s.split()))
    if a**2 + b**2 > c**2:
        r.append("acute triangle")
    elif a**2 + b**2 == c**2:
        r.append("right triangle")
    else:
        r.append("obtuse triangle")
sys.stdout.write("\n".join(r)+"\n")
    
