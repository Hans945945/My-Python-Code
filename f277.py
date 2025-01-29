import sys
n = int(input())
Class_n = []
Names = []
Numbers = []
Ps = []
for s in sys.stdin:
    name, class_n, number, p = s.split()
    Names.append(name)
    Class_n.append(int(class_n))
    Numbers.append(int(number))
    Ps.append(p)
for i in sorted(zip(Class_n,Numbers,Names,Ps)):
    sys.stdout.write(f"{i[0]} {i[1]} {i[2]}\n")
    sys.stdout.write(f"{i[3]}\n")
