import sys
r = []
for s in sys.stdin.readlines():
    word = s.rstrip()
    l = 0
    count = 0
    for i in range(len(word)-1):
        if word[i] == " ":
            count += 1
            if word[i+1] != " " or i == len(word)-2:
                l = max(l,count)
        else:
            count = 0
    ans = 0
    while l > 1:
        if l%2 == 0:
            l //= 2
        else:
            l = l//2 + 1
        ans +=1
    r.append(ans)
sys.stdout.write("\n".join(map(str, r))+"\n")
