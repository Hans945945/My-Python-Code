import sys
segments = [tuple(map(int, s.split())) for s in sys.stdin.readlines()[1:]]
segments.sort()
curr_l, curr_r =segments[0]
total = 0
for l,r in segments[1:]:
    if l <= curr_r:
        curr_r = max(curr_r, r)
    else:
        total += curr_r - curr_l
        curr_r, curr_l = r,l
total += curr_r - curr_l
print(total)
    
