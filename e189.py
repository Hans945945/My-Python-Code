import sys
def Is_three(n):
    even = 0
    odd = 0
    for i in range(0,len(n), 2):
        even += int(n[i])
    for i in range(1, len(n), 2):
        odd += int(n[i])
    r = abs(odd-even)
    if r == 0 or r == 3:
        return True
    elif r < 3:
        return False
    else:
        Is_three(str(r))
for s in sys.stdin:
    n = str(bin(int(s)))[2:]
    print("YES" if Is_three(n) else "NO")
    
