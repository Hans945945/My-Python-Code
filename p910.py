r,c = map(int, input().split())
lunch = [input().split() for _ in range(r)]
q = input()
flag = 1
for i in range(r):
    for j in range(c):
        if lunch[i][j] == q:
             print(i+1,j+1)
             flag = 0
if flag:
    print(0,0)
    
    
