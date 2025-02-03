days = [0,0,31,60,91,121,152,182,213,244,274,305,335]
m,d = map(int, input().split())
d += days[m]
if d <= 20:
    print("Capricorn")
elif d <= 50:
    print("Aquarius")
elif d <= 80:
    print("Pisces")
elif d <= 111:
    print("Aries")
elif d <= 142:
    print("Taurus")
elif d <= 173:
    print("Gemini")
elif d <= 204:
    print("Cancer")
elif d <= 236:
    print("Leo")
elif d <= 267:
    print("Virgo")
elif d <= 297:
    print("Libra")
elif d <= 327:
    print("Scorpio")
elif d <= 357:
    print("Sagittarius")
else:
    print("Capricorn")
