words = input().split()
r = []
for w in words:
    if len(w) == 3 and (w[0] == "F" or w[0] == "f") and (w[1] == "o" or w[1] == "O") and (w[2] == "r" or w[2] == "R"):
        r.append("4")
    elif len(w) == 2 and (w[0] == "T" or w[0] == "t") and (w[1] == "o" or w[1] == "O"):
        r.append("2")
    elif len(w) == 3 and (w[0] == "A" or w[0] == "a") and (w[1] == "n" or w[1] == "N") and (w[2] == "D" or w[2] == "d"):
        r.append("n")
    elif len(w) == 3 and (w[0] == "Y" or w[0] == "y") and (w[1] == "o" or w[1] == "O") and (w[2] == "U" or w[2] == "u"):
        r.append("u")
    else:
        if ord(w[0]) <= 90:
            r.append(w[0])
        else:
            r.append(chr(ord(w[0])-32))
print("".join(r))
