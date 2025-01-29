words = list(input())
for i in range(len(words)):
    print("".join(words))
    words.pop()
