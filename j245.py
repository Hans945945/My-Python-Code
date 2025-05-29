S = input()
if len(S) % 2 == 0:
    S = [S[len(S)//2-1]] + [S[:len(S)//2-1]] + [S[len(S)//2+1:]] + [S[len(S)//2]]
else:
    S = [S[len(S)//2]] + [S[:len(S)//2]] + [S[len(S)//2+1:]] + [S[len(S)//2]]
S = "".join(S)
T = []
a = [str(ord(s)%2) for s in S]
left = -1
right = 0
for i in range(len(S)):
    if a[i] == "0":
        T.append(S[left])
        left -= 1
    else:
        T.append(S[right])
        right +=1
h = bin(int("".join(a[:4]),2) ^ int("".join(str(ord(s)%2) for s in T[:4]),2))[2:].count("1")
print("".join(chr(ord(t)+h) for t in T))
    
