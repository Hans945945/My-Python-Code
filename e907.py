password = input()
r = []
if password.replace("0","").replace("1","") != "":
    r.append("1")
if len(password) < 8 or len(password) > 12:
    r.append("2")
if password.count("0") < 2:
    r.append("3")
if password.count("1") < 3:
    r.append("4")
if "101" not in password:
    r.append("5")
print(" ".join(r) if r else 0)
