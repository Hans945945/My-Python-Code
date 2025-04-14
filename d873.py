import sys
r = []
for s in sys.stdin.readlines():
    r.append(s.rstrip())
    a,op,b = s.split()
    a,b = int(a),int(b)
    if a > 2147483647:
        r.append("first number too big")
    if b > 2147483647:
        r.append("second number too big")
    if (op == "+" and a+b > 2147483647) or (op == "*" and a*b > 2147483647):
        r.append("result too big")
sys.stdout.write("\n".join(r)+"\n")
    
