import sys
for s in sys.stdin:
    a, b, N = map(int, s.split())
    i_len = len(str(a//b))
    a = a* 10**N
    r = list(str(a//b).zfill(i_len+N))
    r.insert(i_len, ".")
    print(''.join(r))
    
    
    
