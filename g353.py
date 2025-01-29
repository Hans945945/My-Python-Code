line = input().split()
print(line[len(line)//2])
while True:
    try:
        input()
    except EOFError:
        break
