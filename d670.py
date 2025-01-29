letters = "0 1 ABC DEF GHI JKL MNO PQRS TUV WXYZ".split()
tele = {}
for i in range(10):
    temp = list(letters[i])
    for j in range(len(temp)):
        tele[temp[j]] = i
tele["-"] = "-"
while True:
    try:
        print("".join(str(tele[i]) for i in input()))
    except EOFError:
        break
