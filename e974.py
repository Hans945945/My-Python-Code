import sys
r,c,n = map(int, input().split())
Class = [[c*i+j+1 for j in range(c)] for i in range(r)]
n-=1
for i in range(n):
    if i %2 == 0:
        for C in Class:
            C.insert(0,C.pop())
    else:
        Class.insert(0,Class.pop())
Class = [" ".join(map(str,row)) for row in Class]
sys.stdout.write("\n".join(Class)+"\n")
