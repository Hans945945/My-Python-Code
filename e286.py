hs1 = sum(list(map(int, input().split())))
as1 = sum(list(map(int, input().split())))
hs2 = sum(list(map(int, input().split())))
as2 = sum(list(map(int, input().split())))
r = 0
if hs1>as1:
    r+=1
elif hs1<as1:
    r-=1
if hs2>as2:
    r+=1
elif hs2<as2:
    r-=1
print(str(hs1)+":"+str(as1))
print(str(hs2)+":"+str(as2))
if r == 2:
    print("Win")
elif r == 0:
    print("Tie")
else:
    print("Lose")
    
