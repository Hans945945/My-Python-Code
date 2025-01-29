while True:
    try:
        n = int(input())
        r = 2
        for i in range(2,n+1):
            r += 2*(i-1)
        print(r)
    except:
         break
