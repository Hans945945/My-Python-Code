import sys
days = [0,0,31,60,91,121,152,182,213,244,274,305,335]
r = []
for s in sys.stdin.readlines():
    m,d = map(int, s.split("/"))
    d += days[m]
    if d <= days[1]+20:
        r.append("摩羯座")
    elif d <= days[2]+19:
        r.append("水瓶座")
    elif d <= days[3]+20:
        r.append("雙魚座")
    elif d <= days[4]+20:
        r.append("牡羊座")
    elif d <= days[5]+21:
        r.append("金牛座")
    elif d <= days[6]+21:
        r.append("雙子座")
    elif d <= days[7]+22:
        r.append("巨蟹座")
    elif d <=days[8]+21:
        r.append("獅子座")
    elif d <= days[9]+23:
        r.append("處女座")
    elif d <= days[10]+23:
        r.append("天秤座")
    elif d <= days[11]+22:
        r.append("天蠍座")
    elif d <= days[12]+22:
        r.append("射手座")
    else:
        r.append("摩羯座")
sys.stdout.write("\n".join(r)+"\n")
