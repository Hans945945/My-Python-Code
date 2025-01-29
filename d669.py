h1,m1,h2,m2 = map(int, input().split())
while not(h1 ==0 and m1 ==0 and h2 ==0 and m2 ==0):
    try:
        m1 += h1*60
        m2 += h2*60
        if m1>m2:
            print(24*60-(m1-m2))
        else:
            print(m2-m1)
        h1,m1,h2,m2 = map(int, input().split())
    except:
        break
