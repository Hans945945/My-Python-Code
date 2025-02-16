import sys
money = 0
cash = []
for s in sys.stdin:
    a,b = map(int, s.split())
    money += a*b
    cash.append((a,b))
cash.sort(reverse = True)
r = [f"{a}元鈔票共有{b}張" for a,b in cash]
r.append(f"總共有{money}元")
sys.stdout.write("\n".join(r)+"\n")
    
