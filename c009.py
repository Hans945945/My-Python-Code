while True:
    n = input()
    if n[0] == "-":
        break
    if n[0:2] == "0x":
        print(int(n, 16))
    else:
        print(f"0x{int(n):X}")
