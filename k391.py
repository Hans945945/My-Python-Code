a,b = input().split()
c,d = input().split()
b = int(b)
d = int(d)
print(f"{a} WIN!" if b > d else f"{c} WIN!" if b < d else "tie")
