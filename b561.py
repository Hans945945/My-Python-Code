import sys
r = []
data = sys.stdin.readlines()
for i in range(0,len(data),2):
    n1 = sum((n/2)**2 for n in map(int, data[i].split()[1:]))*3.14159
    n2 = sum((n/2)**2 for n in map(int, data[i+1].split()[1:]))*3.14159
    r.append(f"{abs(n1-n2):.2f}")
sys.stdout.write("\n".join(r)+"\n")
