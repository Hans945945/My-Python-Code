code = "OIZEASGTBP"
T = int(input())
for i in range(T):
    while True:
        try:
            words = input()
            if words == "":
                break
            for w in words:
                if w.isdigit():
                    print(code[int(w)], end = "")
                else:
                    print(w, end = "")
            print()
        except EOFError:
            break
    print()
    
