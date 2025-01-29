words = input().split()
while words != ["END"]:
    for i in range(len(words)):
        print(chr(ord(words[i][0])-32), end = "")
    print(f' {words[-1]}')
    words = input().split()
