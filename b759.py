text = list(input())
for i in range(len(text)):
    r = "".join(text)
    print(r)
    temp = text.pop(0)
    text.append(temp)
    
