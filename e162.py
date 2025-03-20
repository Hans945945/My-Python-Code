import sys
r = []
for s in sys.stdin.readlines():
    gun = s.strip()
    die = 0
    live = 0
    n = len(gun)
    for i in range(n):
        if gun[i] == "0":
            if gun[(i+1)%n] == "1":
                die += 1
            else:
                live += 1
                
    safe_prob_shoot = live / (live + die) if (live + die) > 0 else 0
    safe_prob_rotate = (live+die) / n

    if safe_prob_shoot == safe_prob_rotate:
        r.append("EQUAL")
    elif safe_prob_shoot > safe_prob_rotate:
        r.append("SHOOT")
    else:
        r.append("ROTATE")
sys.stdout.write("\n".join(r)+"\n")
            
