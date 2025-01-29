while True:
    try:
        n = int(input())
        print((n+2)//3)
    except EOFError:
        break
