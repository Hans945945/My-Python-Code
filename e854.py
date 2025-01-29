goal = input().split()
own = list(input())
r = []
flag = 0
for g in goal:
    for w in g:
        if w in own:
            r.append(own.pop(own.index(w)))
        else:
            flag = 1
            break
    if flag:
        break
    r.append(" ")
print("".join(r).strip())
