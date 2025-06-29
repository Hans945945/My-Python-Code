words = input()
last = ord(words[0])
ans = 0
count = 1
r = []
temp = [words[0]]
for w in words[1:]:
    now = ord(w)
    if now == last + 1:
        count += 1
        temp.append(w)
    else:
        if count >= ans:
            if count == 1:
                temp = [w]
            ans = count
            r = temp.copy()
        count = 1
        temp = [w]
    last = now
print(f"{ans} {''.join(r)}")
