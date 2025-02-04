import sys
r = []
for s in sys.stdin:
    n = s.strip().replace(" ","")
    if n == "0":
        break
    if "+" in n:
        a,b = map(int, n.split("+"))
        r.append(str(a+b))
        r.append("加起來就是團結，團結就是力量，我們五個是最好的朋友!")
    elif "-" in n:
        a,b = map(int, n.split("-"))
        r.append(str(a-b))
        r.append("減並不負面，減只是加一個負數，失去的，終究會回來。我們之間失去的友誼，也終究會回來。生命是美好的，友誼是寶貴的!")
    elif "**" in n:
        a,b = map(int, n.split("**"))
        r.append(str(a**b))
        r.append("乘方就是能力翻倍，我們自己能力翻倍的話，我們五個好朋友的能力就會更強!")
    elif "/" in n:
        a,b = map(int, n.split("/"))
        r.append(f"{a/b:.0f}")
        r.append('除法就是分，我們五個是能平分東西，同甘共苦的好朋友!')
    else:
        a,b = map(int, n.split("*"))
        r.append(str(a*b))
        r.append("正數乘起來會變大，我們五個好朋友在一起，能量也會翻倍!")
sys.stdout.write("\n".join(r)+"\n")
