while 1:
    try:
        a,b,c,d,e = map(int, input().split())
        #b+d = (a+c)*e
        if a < 0:
            print(f"{(b+d)/e-c:.2f}")
        elif b < 0:
            print(f"{(a+c)*e-d:.2f}")
        elif c < 0:
            print(f"{(b+d)/e-a:.2f}")
        elif d < 0:
            print(f"{(a+c)*e-b:.2f}")
        else:
            print(f"{(b+d)/(a+c):.2f}")
    except EOFError:
        break

