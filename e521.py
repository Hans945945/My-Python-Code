import sys
r = []
for s in sys.stdin.readlines()[1:]:
    a,b,c = map(int, s.split())
    if a+b <= c or b+c <= a or a+c <= b:
        r.append("0")
    elif a==b or b==c or a == c:
        r.append("1 1")
    else:
        r.append("1 0")
sys.stdout.write("\n".join(r)+"\n")
