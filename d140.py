import sys
from decimal import Decimal, ROUND_DOWN
for s in sys.stdin:
    price = Decimal(s.strip()) * 100
    if price <= 10000:
        result = price * Decimal("0.9") + (800 if price < 10000 else 0)
    elif price <= 50000:
        result = price * Decimal("0.8")
    else:
        result = price * Decimal("0.6")
    result = (result // 1) / 100
    print(f"${result:.2f}")
