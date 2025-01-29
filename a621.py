n = int(input())
print('2^0 = 1')
r = 1
for i in range(1,n+1):
    r *=2
    print(f'2^{i} = {r}')
    
