a=int(input())
n=False
for i in range(2,a//2+1):
    if a%i==0:
        print('no')
        n=True
        break
if not n:
    print('yes')
