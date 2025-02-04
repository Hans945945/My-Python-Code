original = list(input().lower())
crowd = original.copy()
for i in range(len(crowd)):
    if crowd[i] == " ":
        continue
    crowd[i] = crowd[i].upper()
    print("".join(crowd))
    crowd = original.copy()
