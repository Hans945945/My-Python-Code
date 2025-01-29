while True:
    try:
        def m(n):
            if n <=1:
                print(1, end = " ")
                return 1
            else:
                print(n,"*",end = " ")
                return m(n-1)*n
        n = int(input())
        print(str(n)+"!","=",end = " ")
        total = m(n)
        print("=",total)
        
    except:
        break
