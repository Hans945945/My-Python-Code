words = input()
t = int(input())
if t == 1:
    print(words[0].upper() +words[1:].lower())
elif t == 2:
    print(words.upper())
elif t == 3:
    r = [words[0].upper()]
    upper = 0
    for i in range(1,len(words)):
        if not words[i].isalpha():
            upper = 1
            r.append(words[i])
        else:
            if upper:
                r.append(words[i].upper())
                upper = 0
            else:
                r.append(words[i].lower())
    print("".join(r))
else:
    print(words.lower())
