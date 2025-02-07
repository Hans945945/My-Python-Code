words = input()
shift = int(input())
r = []
for w in words:
    if w.isalpha():
        if w.isupper():
            r.append(chr((ord(w)-65+shift)%26+65))
        else:
            r.append(chr((ord(w)-97+shift)%26+97))
    else:
        r.append(w)
print("".join(r))
