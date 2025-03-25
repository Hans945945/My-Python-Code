import sys
r = []
data = sys.stdin.readlines()
for i in range(0,len(data),2):
    a = data[i].rstrip()
    b = data[i+1].rstrip()
    n1 = sum(ord(w.lower()) - 96 for w in a if w.isalpha())  # a=1, b=2, ..., z=26
    while n1 > 9:
        n1 = sum(map(int, str(n1)))
    n2 = sum(ord(w.lower()) - 96 for w in b if w.isalpha())  # a=1, b=2, ..., z=26
    while n2 > 9:
        n2 = sum(map(int, str(n2)))
    if n1 <= n2:
        r.append(f"{n1/n2*100:.2f} %")
    else:
        r.append(f"{n2/n1*100:.2f} %")
sys.stdout.write("\n".join(r)+"\n")
    
    
