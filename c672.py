import sys
result = []
for s in sys.stdin:
    s = s.strip()
    if s.startswith('#'):
        s = s.lstrip('#')
        r = int(s[0:2], 16)
        g = int(s[2:4], 16)
        b = int(s[4:6], 16)
        result.append(f"{r} {g} {b}")
    else:
        r, g, b = map(int, s.split())
        result.append(f"#{r:02X}{g:02X}{b:02X}")
sys.stdout.write("\n".join(result)+"\n")
