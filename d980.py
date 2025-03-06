import sys
r = []
i = 0
for s in sys.stdin.readlines()[1:]:
    i += 1
    a,b,c = map(int, s.split())
    if a + b <= c or b + c <= a or a+c <= b:
        r.append(f"Case {i}: Invalid")
    elif a == b and b == c:
        r.append(f"Case {i}: Equilateral")
    elif a == b or b == c or a == c:
        r.append(f"Case {i}: Isosceles")
    else:
        r.append(f"Case {i}: Scalene")
sys.stdout.write("\n".join(r)+"\n")
