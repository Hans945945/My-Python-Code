n = int(input())
for _ in range(n):
    for w in input().rstrip(): print(chr((ord(w)+3-65)%26+65), end = "")
    print()
