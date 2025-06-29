import sys
data = sys.stdin.read().split()
for i in range(1,len(data),2):
    a = int(data[i])
    print(a*a//2)

