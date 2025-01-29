while True:
    try:
        n = int(input())
        n = (n+1)//2
        r = (n*(1+1+(n-1)*2)-3)*3
        print(int(r))
    except:
        break
