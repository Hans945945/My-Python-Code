keyboard = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
while True:
    try:
        wrong = input().split()
        correct = []
        for i in range(len(wrong)):
            correct.append("".join([keyboard[keyboard.index(j)-1] for j in wrong[i]]))
        print(" ".join(correct))
    except EOFError:
        break
