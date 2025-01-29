r = []
while True:
    data = input().split()
    if data[0] == "SHOW":
        break
    if data[0] == "ADD":
        r.append(data[1])
    elif data[0] == "INSERT":
        r.insert(r.index(data[2]), data[1])
    else:
        r.pop(r.index(data[1]))
print(" ".join(r))
