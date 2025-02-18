x = int(input())
if x <= -10:
    print(f"{-x**5-33:.1f}")
elif x <= 10:
    print(f"{-0.5*x+10:.1f}")
else:
    print(f"{2*x**0.5:.1f}")
