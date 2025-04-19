import sys
data = sys.stdin.readlines()
idx = 0
r = []
case = 0
while idx < len(data):
    k,e = map(int, data[idx].split())
    idx += 1
    keywords = {data[idx+i].rstrip() for i in range(k)}
    idx += k
    most = 0
    temp = []
    for _ in range(e):
        old = data[idx]
        words = []
        now = []
        for w in old:
            if not w.isalpha():
                words.append("".join(now))
                now = []
            else:
                now.append(w.lower())
        count = sum(1 for w in words if w in keywords)
        if count > most:
            temp = [old]
            most = count
        elif count == most:
            temp.append(old)
        idx += 1
    case += 1
    r.append(f"Excuse Set #{case}")
    r.extend(temp)
    r.append("")
sys.stdout.write("\n".join(r)+"\n")
