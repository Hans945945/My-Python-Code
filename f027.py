import sys
r = []
for s in sys.stdin.readlines()[1:]:
    a,b,c = map(int, s.split())
    if a+b > c and a+c>b and b+c > a:
        r.append("3")
    elif a+b>2*c or b+c>2*a or a+c>2*b:
        r.append("4")
    else:
        r.append("0")
sys.stdout.write("\n".join(r)+"\n") 
