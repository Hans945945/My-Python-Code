import sys
n = int(sys.stdin.readline())
r = []
for s in sys.stdin:
    a,o,b = s.split()
    a = int(a,16)
    b = int(b,16)
    if o == "+":
        total = a+b
    else:
        total = a-b
    r.append(f"{a:013b} {o} {b:013b} = {total}")
sys.stdout.write("\n".join(r)+"\n")
