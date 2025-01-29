from decimal import Decimal
while True:
    try:
        a, b = input().split(".")
        b = Decimal("0."+str(b))
        result = ""
        while b > 0:
            b *= 2
            if b >= 1:
                result += "1"
                b-=1
            else:
                result += "0"
        print(bin(int(a))[2:], result, sep = ".")
    except EOFError:
        break
