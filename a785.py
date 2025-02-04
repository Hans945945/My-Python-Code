import sys
data = sys.stdin.read().splitlines()
table = { "a":{"a":"a", "e":"y", "o":"w"},
          "e":{"a":"a", "e":"ei", "o":"ou"},
          "i":{"a":"ai", "e":"ei", "o":"oi"},
          "y":{"a":"a", "e":"y", "o":"w"},
          "o":{"a":"w", "e":"ou", "o":"ou"},
          "u":{"a":"w", "e":"ou", "o":"ou"}, #用u代替ou當索引（程式會需要微調）
          "w":{"a":"w", "e":"w", "o":"w"}
        }
r = []
for s in data[:-1]:
    a,b = s.split("-")
    if b[:2] == "ou":
        b = b[1:]
    new = table[b[0]][a[-1]]
    r.append(a[:-1]+new+b[1:])
sys.stdout.write("\n".join(r)+"\n")
