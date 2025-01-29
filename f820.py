import sys
n = int(sys.stdin.readline())
Mt = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())
t-=1
if t == 0 or t != n-1 and Mt[t-1] > Mt[t+1] :
    for i in range(t+1, n):
        if Mt[i] > Mt[i-1]:
            print(i)
            break
else:
    for i in range(t-1, -1, -1):
        if Mt[i-1] > Mt[i]:
            print(i+1)
            break
