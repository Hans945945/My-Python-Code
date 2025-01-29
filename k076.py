bases = list(map(int, input().split()))+[0,0,0,0]
h = int(input())
bases[3] = 1
print(sum(bases[:h])*(h!=0))
print(" ".join(list(map(str, bases[h:h+3]))))



    
