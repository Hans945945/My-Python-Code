while True:
    a,b = map(int, input().split())
    if a==0 and b == 0:
        break
    r = list(map(int, str(a+b)))
    num1 = list(map(int, str(a)))
    num2 = list(map(int, str(b)))
    while len(num1) < len(num2):
        num1.insert(0, 0)
    while len(num2) < len(num1):
        num2.insert(0, 0)
    Carry = 0 #True, False
    carry = 0
    for i in range(len(num1)-1,-1,-1):
        if num1[i] + num2[i]+Carry >= 10:
            carry += 1
            Carry = 1
        else:
            Carry = 0
    if carry == 0:
        print("No carry operation.")
    elif carry == 1:
        print("1 carry operation.")
    else:
        print(f"{carry} carry operations.")
        
    
