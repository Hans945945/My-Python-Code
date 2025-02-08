import sys
A = {0:0,1:0,2:0,3:0}
for s in sys.stdin.readlines()[1:]:
    a,b = map(int, s,split())
    A[a] += b
print(A[1] - A[3], A[0] - A[2])
