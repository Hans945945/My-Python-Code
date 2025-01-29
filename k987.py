import sys
input()
for s in sys.stdin:
    n,k = map(int, s.split())
    seen = set()
    max_value = 0
    limit = 10**n
    while k not in seen:
        seen.add(k)
        max_value = max(max_value, k)
        if max_value == limit-1:
            break
        k *= k
        k = int(str(k)[:n])
    print(max_value)
    
