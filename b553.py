import sys
r = []
for s in sys.stdin.readlines():
    if s == "\n":
        break
    n = int(s)
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:
            n//= 2
        else:
            n = n*3+1
    r.append(count)
sys.stdout.write("\n".join(map(str, r))+'\n')
    
