while True:
    fo, fe, FA = map(float, input().split())
    if fo == 0 and fe == 0 and FA == 0:
        break
    M = fo/fe
    FT = FA / M
    print(f"{M:.2f} {FT:.2f}")
