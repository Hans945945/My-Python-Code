import sys
r = []
case = 0
films = []
for s in sys.stdin.readlines()[1:]:
    case += 1
    now = s.split()
    a = now[0]
    p,l,w,r = map(int, now[1:])
    score = p*w/l*r
    films.append((-score,case,a))
films.sort()
sys.stdout.write("\n".join(n for _,_,n in films)+"\n")
    
