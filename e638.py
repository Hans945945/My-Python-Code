while True:
    try:
        num = "00000"
        while num[-1] != "#":
            num += input()
        print("YES" if int(num.rstrip("#"), 2) % 131071 == 0 else "NO")
    except EOFError:
        break
