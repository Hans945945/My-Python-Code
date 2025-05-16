s = input()
for k in range(26):
    if "love" in s or "Love" in s:
        print(k)
        break
    new = list(s)
    for i in range(len(s)):
        if new[i].isupper():
            new[i] = chr((ord(s[i])-65+1)%26+65)
        elif new[i].islower():
            new[i] = chr((ord(s[i])-97+1)%26+97)
    s = "".join(new)
