import unicodedata
import sys
r = []
for s in sys.stdin:
    r.append("".join(w for w in s.strip() if unicodedata.name(w)[:3] == "CJK"))
sys.stdout.write("\n".join(r)+"\n")
