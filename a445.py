'''
TLE

def is_friend(a,b):
    q = [a]
    visited = [0 for _ in range(n+1)]
    while q:
        now = q.pop(0)
        visited[now] = 1

        for next_node in friends[now]:
            if next_node == b:
                return 1
            if visited[next_node] == 0:
                visited[next_node] = 1
                q.append(next_node)
    return 0

n,m,q = map(int, input().split())
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
for _ in range(q):
    a,b = map(int, input().split())
    print(':)' if is_friend(a,b) else ":(")

'''
from collections import deque

def find(x):
    if friends[x] != x:
        friends[x] = find(friends[x])
    return friends[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        friends[y] = x

n,m,q = map(int, input().split())
friends = list(range(n+1))

for _ in range(m):
    a,b = map(int, input().split())
    union(a,b)
    
for _ in range(q):
    a,b = map(int, input().split())
    print(':)' if find(a) == find(b) else ":(")
    
