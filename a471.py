import math 
while True:
    try:
        n = int(input())
        total = 0
        factors1 = []
        factors2 = []
        s = 0
        for i in range(2, int(math.sqrt(2*n))+1):
            if 2*n%i == 0:
                factors1.append(i)
                factors2.append((2*n)//i)
        factors1.reverse()
        factors2.reverse()
        for i in range(len(factors1)):
            p = factors2[i]
            q = factors1[i]
            a = (p+q-1)/2
            b = (p-q+1)/2
            if a %1 ==0 and b%1 == 0:
                print(int(b),"-",int(a), sep = "")
                s = 1

        if s == 0:
            print("No Solution...")
    except:
        break
