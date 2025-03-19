import sys
r = []
for s in sys.stdin.readlines()[1:]:
    word = s.rstrip()
    sqrt = len(word)**0.5
    if sqrt.is_integer():
        sqrt = int(sqrt)
        r.append("".join("".join(word[j] for j in range(i,len(word),sqrt)) for i in range(sqrt)))
    else:
        r.append("INVALID")
sys.stdout.write("\n".join(r)+"\n")
