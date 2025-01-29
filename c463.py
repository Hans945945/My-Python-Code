from collections import defaultdict
def H(p):
    if len(tree[p]) == 0:
        return 0
    
    if h[p] == -1:
        m = 0
        
        for v in tree[p]:
            now = H(v)
            m = max(m, now+1)
        return m
    else:
        return h[p]

n = int(input())
tree = defaultdict(list)
is_root = [1 for _ in range(n + 1)]
is_root[0] = 0  

for i in range(1, n+1):
    temp = list(map(int, input().split()))[1:]
    for child in temp:
        is_root[child] = 0
    tree[i].extend(temp)

root = is_root.index(1)

h = [-1]*(n+1)
h[0] = 0
for i in range(n, 0, -1):
    h[i] = H(i)

print(root)
print(sum(h))
    

