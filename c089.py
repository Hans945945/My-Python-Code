import sys

digits = "0123456789ABCDEF"

for s in sys.stdin:
    parts = s.split()
    N = parts[0].upper()
    To = int(parts[2])
    temp = int(N, int(parts[1]))
    
    if To == 10:
        ans = str(temp)
    else:
        if temp == 0:
            ans = "0"
        else:
            ans = ""
            while temp > 0:
                ans = digits[temp % To] + ans
                temp //= To
                
    if len(ans) > 7:
        print("  ERROR")
    else:
        print(ans.rjust(7))
