import sys
data = sys.stdin.readlines()
r = []
for i in range(0,len(data),2):
    r.append(str((ord(data[i+1][0]) - ord(data[i][0]) + 26)%26))
sys.stdout.write("\n".join(r)+"\n")
