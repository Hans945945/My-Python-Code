import sys

def convert(n,temp):
    for v, u in [(10000000, "kuti"), (100000, "lakh"), (1000, "hajar"), (100, "shata")]:
        if n >= v:
            convert(n // v, temp)
            temp.append(u)
            n %= v
    if n:
        temp.append(f"{n}")

r = []
case = 1
for s in sys.stdin:
    n = int(s)
    if n == 0:
        r.append(f"{case}. 0")
    else:
        temp = []
        convert(n,temp)
        r.append(f"{case}. {' '.join(temp)}")
    case += 1
sys.stdout.write("\n".join(r)+"\n")


    
