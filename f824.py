import sys
r = []
table = {"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10}
table2 = {v: k for k, v in table.items()}
for s in sys.stdin.readlines():
    a,b = table[s[0]], table[s[2]]
    if s[1] == "又" or s[1] == "有":
        temp = a+b
        r.append("二十" if temp == 20 else f"十{table2[temp-10]}"if temp > 10 else table2[temp])
    else:
        r.append("謬")
sys.stdout.write("\n".join(r)+"\n")
