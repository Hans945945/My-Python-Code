import sys
r = []
for s in sys.stdin.readlines()[:-1]:
    nums = [len(w) for w in s.split()[:-1]]
    flag = -1
    ans = []
    for n in nums:
        if n == 1:
            flag = "1"
        elif n == 2:
            flag = "0"
        else:
            ans.extend(flag*(n-2))
    r.append(str(int("".join(ans),2)))
sys.stdout.write("\n".join(r)+"\n")
