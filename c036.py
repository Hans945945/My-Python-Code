import sys
r = []
for s in sys.stdin.readlines()[:-1]:
    h,u,d,f = map(int, s.split())
    l = 0
    day = 0
    f = u*(f/100)
    while True:
        l += u
        day += 1 
        u -= f
        if u < 0:
            u = 0
        if l > h:
            r.append(f"success on day {day}")
            break
        l -= d
        if l < 0:
            r.append(f"failure on day {day}")
            break
        
sys.stdout.write("\n".join(r)+"\n")
            
