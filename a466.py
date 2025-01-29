n = int(input())
for _ in range(n):
    text = list(input())
    if len(text) == 5:
        print(3)
    else:
        if (text[0] == "o" and text[1] == "n") or (text[0] == "o" and text[2] == "e") or (text[2] == "e" and text[1] == "n"):
            print(1)
        else:
            print(2)
