a,b,c = map(int, input().split())
count = 0
for i in range(1,c+1):
    if i%a == 0 or i%b == 0:
        count += i
print(chr((count-1)%26+65))
