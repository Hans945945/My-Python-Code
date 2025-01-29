while True:
    try:
        V, R = map(float, input().split())
        print(f"{V/R*1000:.4f}")
    except EOFError:
        break
