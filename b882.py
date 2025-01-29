H,M,S = map(int, input().split())
M += S//60
S %= 60
H += M // 60
M %= 60
H = H%24
while len(str(H)) == 1:
    H = "0"+str(H)
while len(str(M)) == 1:
    M = "0"+str(M)
while len(str(S)) == 1:
    S = "0"+str(S)
print(f"{H}:{M}:{S}")
    
