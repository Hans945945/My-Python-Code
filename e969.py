import sys
n,m,k = map(int, sys.stdin.readline().split())
price = 55*k+32*(not k)
r = []
time = 0
while n >= price:
    n-=price
    if n == 0:
        a = "doesn't have money."
    elif n == 1:
        a = f"has 1 dollar."
    else:
        a = f"has {n} dollars."
    if price == 32:
        r.append(f"{time}: Wayne eats an Apple pie, and now he {a}")
    else:
        r.append(f"{time}: Wayne drinks a Corn soup, and now he {a}")
    time += m
    k = abs(k-1)
    price = 55*k+32*(not k)
if len(r) == 0:
    r.append("Wayne can't eat and drink.")
sys.stdout.write("\n".join(r)+"\n")
