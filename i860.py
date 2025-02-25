import sys
r = []
for s in sys.stdin.readlines()[1:]:
    m,y,c,color = s.split()
    m = int(m)
    y = int(y)
    c = int(c)
    flag = 0
    for w in color:
        if w == "M":
            m -= 1
        elif w == "Y":
            y-=1
        elif w == "C":
            c -= 1
        elif w == "R":
            m-=1
            y-=1
        elif w == "B":
            m-=1
            y-=1
            c-=1
        elif w == "G":
            y-=1
            c-=1
        elif w == "V":
            m-=1
            c-=1
        if m < 0 or y < 0 or c < 0:
            flag = 1
            break
    r.append('NO' if flag else f'YES {m} {y} {c}')
sys.stdout.write("\n".join(r)+"\n")

            
