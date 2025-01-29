n = int(input())
for _ in range(n):
    s = input()
    if s == "1" or s == "4" or s == "78":
        print("+")
    elif len(s) > 2 and s[-1] == "5" and s[-2] == "3":
        print("-")
    elif len(s)>1 and s[0] == "9" and s[-1] == "4":
        print("*")
    else:
        print("?")
