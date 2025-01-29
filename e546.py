while True:
    try:
        n,r = map(int, input().split())
        Return = list(map(int, input().split()))
        if n == r:
            print("*")
        else:
            ids = [i for i in range(1,n+1)]
            dead = [x for x in ids if x not in Return]
            print(' '.join(map(str, dead)))
    except EOFError:
        break
