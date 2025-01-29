import sys
for s in sys.stdin:
    s = int(s)
    if s == 0:
        break
    for i in range(s*8):
        if i % (s*2) < s:
            for j in range(4):
                print("".join(["#" for _ in range(s)]), end = "")
                print("".join(["." for _ in range(s)]), end = "")
        else:
            for j in range(4):
                print("".join(["." for _ in range(s)]), end = "")
                print("".join(["#" for _ in range(s)]), end = "")
        print()
    print()
    
                
        
