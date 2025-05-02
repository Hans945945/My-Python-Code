import sys
data = sys.stdin.readlines()
r = []

for i in range(0, len(data), 2):
    n, m = map(int, data[i].split())
    cards = data[i + 1].split()
    count = 0
    side = 1 
    now = 1

    for c in cards:
        if c == "A":
            count = 0
        elif c == "4":
            side *= -1
        elif c.startswith("5("):
            now = int(c[2:-1])
            continue
        elif c == "10+":
            count += 10
        elif c == "10-":
            count = max(0, count - 10)
        elif c == "J":
            pass
        elif c == "Q+":
            count += 20
        elif c == "Q-":
            count = max(0, count - 20)
        elif c == "K":
            count = 99
        else:
            count += int(c)

        if count > 99:
            r.append(f"{now} cheated!")
            break

        now += side
        if now < 1:
            now = n
        elif now > n:
            now = 1

    if len(r) == i // 2:
        r.append(f"The sum is {count}")
        
sys.stdout.write("\n".join(r)+"\n")
