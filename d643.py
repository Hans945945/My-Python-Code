import sys
import re
w = "".join(s.strip() for s in sys.stdin.readlines())
n = len(w)
nums = [1]
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        nums.append(i)
        if n //i != i:
            nums.append(n//i)
nums.sort()
seen = [w]
for n in nums:
    temp = "".join(sorted(re.findall(f".{{1,{n}}}", w)))
    if temp not in seen:
        seen.append(temp)
        
seen.pop(0)
sys.stdout.write("\n".join(seen)+"\n" if seen else "bomb!")
