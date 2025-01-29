import sys
a = ("鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬")
for s in sys.stdin:
    s = int(s)
    if s > 0:
        print(a[(s%12)-1])
    else:
        print(a[(s%12)])
