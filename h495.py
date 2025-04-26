import sys
r = []
for s in sys.stdin.readlines()[1:]:
    a,b,c,d,e,f,g,h,i,j,k,l,m = map(int, s.split())
    score = -h + i + j + 2*k + 3*l + m
    score += 4 if a > 4 else 3 if a == 4 else 2 if a == 3 else 1 if a == 2 else -1
    score += 4 if b > 3 else 3 if b == 3 else 2 if b == 2 else 1 if b == 1 else -1
    score += 4 if c > 7 else 3 if c >= 6 else 2 if c >= 4 else 1 if c >= 1 else -1
    score += 4 if d > 3 else 3 if d == 3 else 2 if d == 2 else 1 if d == 1 else -1
    score += 4 if e > 7 else 3 if e >= 6 else 2 if e >= 4 else 1 if e >= 1 else -1
    score += 4 if f > 6 else 3 if f >= 5 else 2 if f >= 3 else 1 if f >= 1 else -1
    score += 4 if g > 5 else 3 if g >= 4 else 2 if g >= 2 else 1 if g == 1 else -1
    r.append(str(score))
sys.stdout.write("\n".join(r)+"\n")
