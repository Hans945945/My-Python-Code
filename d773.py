import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
r = []
for i,num in enumerate(nums):
    power = n - i
    if num == 0:
        continue
    if num > 0:
        num = "+"+str(num)
    if power > 1:
        r.append(f"{num if abs(int(num)) != 1 else '+' if int(num) > 0 else '-'}x^{power}")
    elif power == 1:
        r.append(f"{num if abs(int(num)) != 1 else '+' if int(num) > 0 else '-'}x")
    else:
        r.append(f"{num}")
r = "".join(r)
if r[0] == "+":
    sys.stdout.write(r[1:]+"\n")
else:
    sys.stdout.write(r+"\n")
    
    

