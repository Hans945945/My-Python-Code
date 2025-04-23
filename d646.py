a,b = int(input(),2), int(input(),2)
while b:
    a,b = b,a%b
print(bin(a)[2:])
