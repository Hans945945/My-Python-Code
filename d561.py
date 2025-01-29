import decimal
import sys
r = []
for s in sys.stdin:
    num = decimal.Decimal(s.strip())
    temp = f"{num:.2f}"
    r.append("0.00" if temp == "-0.00" else temp)
sys.stdout.write("\n".join(r)+"\n")
