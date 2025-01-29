words = []
length = []
while True:
    try:
        temp = list(input())
        words.append(temp)
        length.append(len(temp))
    except EOFError:
        break
for i in range(max(length)):
    for j in range(len(words)-1,-1,-1):
        if i >= length[j]:
            if length.index(max(length)) >j and i == max(length)-1:
                break
            else:
                print(" ", end = "")
        else:
            print(words[j][i],end = "")
    print()
