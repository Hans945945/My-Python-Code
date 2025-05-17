from collections import defaultdict

MAP = defaultdict(list)

for i, (u, v) in enumerate([(1,5), (1,3), (1,2), (2,5), (2,3), (3,5), (4,5), (4,3)]):
    MAP[u].append((v, i))
    MAP[v].append((u, i))

r = []

def dfs(node, path, visited):
    if len(path) == 9:
        r.append(''.join(map(str, path)))
        return
    for Next, Id in sorted(MAP[node]):
        if not visited[Id]:
            visited[Id] = 1
            path.append(Next)
            dfs(Next, path, visited)
            path.pop()
            visited[Id] = 0

visited = [0] * 8
dfs(1, [1], visited)
r.sort()

print("\n".join(r))

