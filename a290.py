import sys
while True:
    try:
        n,m = map(int, input().split())
        city = [[] for _ in range(n+1)]
        for _ in range(m):
            a,b = map(int, sys.stdin.readline().split())
            city[a].append(b)
        A,B = map(int, input().split())
        Q = [A]
        visited = [0 for _ in range(n+1)]
        while len(Q) > 0:
            now = Q.pop(0)
            visited[now] = 1
            
            for Next in city[now]:
                if not visited[Next]:
                    visited[Next] = 1
                    Q.append(Next)
        print("Yes!!!" if visited[B] else "No!!!")
    except EOFError:
        break
