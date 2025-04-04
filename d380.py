import sys
data = sys.stdin.readlines()
sys.stdout.write("\n".join(str(int(data[i])*int(data[i+1])) for i in range(0,len(data),2))+"\n")
