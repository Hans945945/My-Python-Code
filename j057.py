import sys
for s in sys.stdin:
    S0 = int(s)
    if S0 == 0:
        break
    n = 4
    seen = set()
    count = 0
    while S0 not in seen:
        seen.add(S0)
        count += 1
        S0_squared = S0 * S0
        S0_str = str(S0_squared).zfill(2 * n)
        mid_start = len(S0_str) // 2 - n // 2
        S0 = int(S0_str[mid_start:mid_start + n])
        
    print(count)
