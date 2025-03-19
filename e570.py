import sys
r = []
for s in sys.stdin.readlines():
    word = s.strip()
    if "是" in word:
        a,b,c = word.partition("是")
        r.append(f"{c}{a}")
    else:
        a,b,c = word.partition("之")
        r.append(f"{c}{a}")
sys.stdout.write("\n".join(r)+"\n")
