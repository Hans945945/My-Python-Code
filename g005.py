code = input()
start = 0
r = list(code)
for i in range(len(code)-1):
    if code[i] == "-" or code[i] == "+":
        if code[i] == "-" and code[i+1].isalnum():
            start = i+1
        elif start != 0:
            last = i
            r[start:last] = code[start:last][::-1]
            start = 0
if start != 0:
    last = len(code)
    r[start:last] = code[start:last][::-1]
    start = 0
print("".join(r).replace("-", "").replace("+",""))
            
            
            
