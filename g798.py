import sys
old = list(map(int, sys.stdin.readline().split()))[:-1]
n = int(sys.stdin.readline())
for _ in range(n):
    stores = old.copy()
    if old[0]>old[1]:
        stores[1]+=old[0]//10
    for i in range(1,len(old)-1):
        if old[i]>old[i+1]:
            stores[i+1] += old[i]//20
        if old[i]>old[i-1]:
            stores[i-1] += old[i]//20
    if old[-1]>old[-2]:
        stores[-2]+=old[-1]//10
    old = stores
sys.stdout.write(" ".join(map(str, old))+"\n")
