n = list(input())
if n[0] == "-":
    n.pop(0)
    print("-", end = "")
n.reverse()
print(int(''.join(n)))
    
    
