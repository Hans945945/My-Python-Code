import sys
data = sys.stdin.readlines()
sys.stdout.write("\n".join(max(data[i].split(),key = int) for i in range(1,len(data),2))+"\n")
