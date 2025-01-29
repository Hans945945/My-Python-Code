N,K = map(int,input().split())
Ns = list(map(int,list(str(N))))
if N%K == 0 or Ns.count(K) != 0:
    print("YES")
else:
    print("NO")
    
