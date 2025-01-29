words = input().split()
for i in range(len(words)-1):
    print(words[i], "little, ", end = "")
print(f"{words[-1]} little Indians")
