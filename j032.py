import sys
r = []
for s in sys.stdin.readlines()[:-1]:
    i = -1
    a = 0
    b = 0
    j = 0
    for w in bin(int(s))[2:][::-1]:
        i+=1
        if w == "0":
            continue
        if j % 2 == 0:
            a += 2**i
        else:
            b += 2**i
        j+=1
    r.append(f"{a} {b}")
sys.stdout.write("\n".join(r)+"\n")
