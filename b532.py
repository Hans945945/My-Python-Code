import sys
r = []
for s in sys.stdin.readlines()[1:]:
    temp = []
    o = ""
    for w in s:
        if w == "+" or w == "-" or w == "*" or w == "/" or w == "%":
            o = w
            a = int("".join(temp))
            temp = []
        elif w.isdigit():
            temp.append(w)
    b = int("".join(temp))
    if o == "+":
        r.append(a+b)
    elif o == "-":
        r.append(a-b)
    elif o == "*":
        r.append(a*b)
    elif o == "/":
        r.append(a//b)
    else:
        r.append(a%b)
sys.stdout.write("\n".join(map(str, r))+"\n")
