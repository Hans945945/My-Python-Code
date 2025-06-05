from fractions import Fraction
data = input().split()
ans = Fraction(data[0])
for i in range(1,len(data),2):
    o = data[i]
    a = Fraction(data[i+1])
    if o == "+":
        ans += a
    else:
        ans -= a
print(f"{ans}/1" if ans == 1 or ans == 0 else ans)
