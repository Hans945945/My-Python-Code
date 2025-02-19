import sys
def GCD(a,b):
    while b:
        a,b = b,a%b
    return a
r = []
data = sys.stdin.readlines()[1:]
for i in range(0,len(data),2):
    S1 = int(data[i],2)
    S2 = int(data[i+1],2)
    r.append(f"Pair #{i//2+1}: All you need is love!" if GCD(S1,S2) != 1 else f"Pair #{i//2+1}: Love is not all you need!")
sys.stdout.write("\n".join(r)+"\n")
