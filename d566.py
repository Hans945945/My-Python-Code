import sys
data = sys.stdin.readlines()
if len(data) == 1:
    data = data[0].split()
    n = int(data.pop(0))
    data = [f"{data[i]} {data[i+1]}" for i in range(0,2*n,2)]
else:
    n = int(data.pop(0))
people = set()
AC = set()
first_time_pass = 0
for temp in data[::-1]:
    p,s = temp.split()
    if s == "AC":
        if p not in people:
            first_time_pass += 1
        AC.add(p)
    people.add(p)
print(f"{first_time_pass * 100 // len(AC)}%")
