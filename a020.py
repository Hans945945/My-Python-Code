a = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":34,"J":18,"K":19,"L":20,"M":21,"N":22,"O":35,"P":23,"Q":24,"R":25,"S":26,"T":27,"U":28,"V":29,"W":32,"X":30,"Y":31,"Z":33}
ID = list(input())
L = a[ID[0]]
num = (L%10)*9+L//10
ID.pop(0)
ID = list(map(int,ID))
last_num = ID.pop()
for i in range(8):
    ID[i] = ID[i]*(8-i)
ID.append(last_num)
ID.append(num)
total = sum(ID)
if total % 10 == 0:
    print("real")
else:
    print("fake")

