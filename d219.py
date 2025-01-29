while True:
    try:
        b,p,m = map(int, input().split())
        print(pow(b,p,m))
    except EOFError:
        break
