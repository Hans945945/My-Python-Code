N = int(input())
i = 1
while N>4*i*(i+1)//2:
    i+=1
    a=(4*i*(i+1)//2-N)//i
print("Pineapple pen" if a == 0 else "Apple" if a == 1 else "Pineapple" if a == 2 else "Pen")
