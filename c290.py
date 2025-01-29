
Num = int(input())
A = 0
B = 0
count = 1
while Num >= 10:
    if count %2 == 0:
        B += Num % 10
    else:
        A += Num % 10
    count += 1
    Num = Num //10
if count %2 == 0:
    B += Num % 10
else:
    A += Num % 10
print(abs(A-B))
    
