word = input()
T = int(input())
for _ in range(T):
    a = int(input())
    r = []
    if a == 0:
        for i in range(0,len(word),2):
            r.extend([word[i+1], word[i]])
    elif a == 1:
        for i in range(0, len(word),2):
            r.extend(sorted([word[i], word[i+1]]))
    else:
        m = len(word)//2
        for i in range(m):
            r.extend([word[i], word[i+m]])
    word = "".join(r)
print(word)
