h, m = map(int, input().split())
m += h*60
if m >= 450 and m < 17*60:
    print("At School")
else:
    print("Off School")
