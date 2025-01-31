from itertools import permutations
def math(i,number,b):
    if i == 0:
        number += b
    elif i == 1:
        number -= b
    else:
        number *= b
    return number
nums = list(map(int, input().split()))
while sum(nums) != 0:
    p = 0
    for a,b,c,d,e in permutations(nums,5):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        number = a
                        number = math(i,number,b)
                        number = math(j,number,c)
                        number = math(k,number,d)
                        number = math(l,number,e)
                        if number == 23:
                            print("Possible")
                            p = 1
                            break
                    if p:
                        break
                if p:
                    break
            if p:
                break
        if p:
            break
    
    if p == 0:
        print("Impossible")
    nums = list(map(int, input().split()))
