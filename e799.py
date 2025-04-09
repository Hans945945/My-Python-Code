import sys
data = sys.stdin.readlines()
n,m = map(int, data[0].split())
c = data[1].strip() 
sys.stdout.write("\n".join(" ".join(c if w == "1" else "." for w in bin(int(data[i]))[2:].zfill(m)) for i in range(2,n+2))+"\n")
