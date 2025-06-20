while True:
    try:
        s = input()
        last = s[0]
        r = []
        first = 1
        for w in s[1:]:
            if (w == " " or first) and last == " ":
                r.append("*")
            else:
                r.append(last)
            if first:
                first = 0
            last = w
        r.append(last if last != " " else "*")
        print("".join(r))
    except EOFError:
        break
