import sys
data = sys.stdin.read().splitlines()
data.pop(0)
x = 0
count = 0
for s in data:
    order = s.strip()
    if order == "L":
        x -= 1
    elif order == "R":
        x += 1
    elif int(order[5:]) == x:
        count += 1
print(count)
        
