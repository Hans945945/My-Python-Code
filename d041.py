import sys
data = sys.stdin.readlines()
T = int(data.pop(0))
r = []
for i in range(0,T*3,3):
    d1,m1,y1 = map(int, data[i+1].split("/"))
    d2,m2,y2 = map(int, data[i+2].split("/"))
    age = y1-y2 - (m1<m2) - (m1 == m2 and d1 < d2)
    r.append(f"Case #{i//3+1}: Invalid birth date" if age < 0 else f"Case #{i//3+1}: Check birth date" if age > 130 else f"Case #{i//3+1}: {age}")
sys.stdout.write("\n".join(r)+"\n")      
