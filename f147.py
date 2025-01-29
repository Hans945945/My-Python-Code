a1 = ["Medium Wac","WChicken Nugget","Geez Burger","ButtMilk Crispy Chicken","Plastic Toy"]
a2 = ["German Fries","Durian Slices","WcFurry","Chocolate Sunday"]
total = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        t = int(input())
        price = (t==1)*4+(t==2)*8+(t==3)*7+(t==4)*6+(t==5)*3
        total += price
        print(a1[t-1], price)
    else:
        t = int(input())
        price = (t==1)*2+(t==2)*3+(t==3)*5+(t==4)*7
        total += price
        print(a2[t-1], price)
print('Total:',total)
