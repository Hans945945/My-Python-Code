import sys
data = sys.stdin.read().split()
table = {"A":[1,0],"B":[1,1],"C":[1,2],"D":[1,3],"E":[1,4],
         "F":[1,5],"G":[1,6],"H":[1,7],"I":[3,4],"J":[1,8],
         "K":[1,9],"L":[2,0],"M":[2,1],"N":[2,2],"O":[3,5],
         "P":[2,3],"Q":[2,4],"R":[2,5],"S":[2,6],"T":[2,7],
         "U":[2,8],"V":[2,9],"W":[3,2],"X":[3,0],"Y":[3,1],"Z":[3,3]}
idx = 0
r = []
while idx < len(data):
    n = int(data[idx])
    idx += 1
    seen = set()
    T = O = F = 0
    for _ in range(n):
        Id = data[idx].strip()
        idx += 1
        if Id in seen:
            O += 1
            continue
        change = table[Id[0]]
        now = change[0]*1+change[1]*9
        for i in range(8):
            now += int(Id[i+1])*(8-i)
        now += int(Id[-1])
        if now%10 == 0 and (Id[1] == "1" or Id[1] == "2"):
            seen.add(Id)
            T += 1
        else:
            F += 1
    r.append(f"{T},{O},{F}")
sys.stdout.write("\n".join(r)+"\n")
                
        
