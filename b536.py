import sys

r = []
for s in sys.stdin.readlines()[1:]:
    s = s.strip().replace("-", "")
    if len(s) == 10:
        digits = s[:9]
        old = s[9]
        total = 0
        for i in range(9):
            total += int(digits[i]) * (10-i)
        mod = 11 - (total % 11)

        check = 'X' if mod == 10 else "0" if mod == 11 else str(mod)

        r.append("T" if check == old else "F")
        
    elif len(s) == 13:
        digits = s[:12]
        old = int(s[12])
        total = 0
        for i in range(12):
            weight = 1 if i % 2 == 0 else 3
            total += int(digits[i]) * weight
        check = (10 - (total % 10)) % 10
        r.append("T" if check == old else "F")
    else:
        r.append("F")
        
sys.stdout.write("\n".join(r) + "\n")
