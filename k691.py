import sys
T = int(input())
r = []
for s in sys.stdin:
    n = s.strip()
    if "+" in n:
        a,b = map(int, n.split("+"))
        r.append(a+b)
    elif "-" in n:
        a,b = map(int, n.split("-"))
        r.append(a-b)
    elif "**" in n:
        a,b = map(int, n.split("**"))
        r.append(a**b)
    elif "/" in n:
        a,b = map(int, n.split("/"))
        r.append(a//b)
    elif "*" in n:
        a,b = map(int, n.split("*"))
        r.append(a*b)
    else:
        r.append(int(int(n[5:])**0.5))
sys.stdout.write("\n".join(map(str, r)))
