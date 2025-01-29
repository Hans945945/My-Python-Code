count = 0
while True:
    try:
        data = input().split("=")
        c = data.pop()
        if c == "?":
            continue
        else:
            c = int(c)
        if "+" in data[0]:
            a, b = map(int, data[0].split("+"))
            if a + b == c:
                count += 1  
        else:
            a, b = map(int, data[0].split("-"))
            if a - b == c:
                count += 1
    except EOFError:
        break
print(count)
