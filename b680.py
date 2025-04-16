N = int(input())
players = [tuple(map(float, input().split())) for _ in range(N)]
players.sort(key=lambda x: x[1])

G = N // 8
order = []
while len(order) < N:
    order += list(range(1, G + 1)) + list(range(G, 0, -1))

groups = {i: [0]*8 for i in range(1, G + 1)}
lane_map = [(0, 3), (1, 4), (2, 2), (3, 5), (4, 1), (5, 6), (6, 0), (7, 7)]

for i, (p, _) in enumerate(players):
    group = order[i]
    groups[group][lane_map[len([x for x in order[:i] if x == group])][1]] = int(p)

for i in sorted(groups):
    print(i, *groups[i])
