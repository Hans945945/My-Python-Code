while True:
    data = input().split()
    if data == ["END"]:
        break
    star = data.pop(0)
    mB, mV = map(float, data)
    B = mB-mV
    if B >= 1.5:
        r = "M"
    elif B >= 1:
        r = "K"
    elif B >= 0.5:
        r = "G"
    elif B >= 0.25:
        r = "F"
    elif B >=0:
        r = "A"
    elif B >= -0.25:
        r = "B"
    else:
        r = "O"
    print(f"{star} {B:.2f} {r}")
    
