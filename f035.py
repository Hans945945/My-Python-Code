words = list(input())
print("_".join([str(ord(words[i])) for i in range(len(words))]))
