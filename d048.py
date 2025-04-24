import sys
r = []
for s in sys.stdin.readlines()[1:]:
    h,m = map(int, s.split(":"))
    hh,mm = h,m
    while 1:
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        temp = str(mm) if hh == 0 else f"{hh}{mm:02d}"
        if temp == temp[::-1]:
            break
    r.append(f"{hh:02d}:{mm:02d}")
sys.stdout.write("\n".join(r)+"\n")
