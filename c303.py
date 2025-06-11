import sys
data = sys.stdin.readlines()
for i in range(1,len(data),2):
    print("".join(w.upper() if w.islower() else w.lower() for w in data[i]))
