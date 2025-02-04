import sys
r = []
for s in sys.stdin:
    s = int(s[2:],16)
    temp = chr(s)
    s = f"{s:016b}"
    r.append(f"1110{s[0:4]} 10{s[4:10]} 10{s[10:16]}")
    r.append(temp)
sys.stdout.write("\n".join(r)+"\n")
