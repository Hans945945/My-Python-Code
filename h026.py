F = input()
N = int(input())
sister = input().split()
brother = [F]
status = "Drew"
Round = N
opposite = {"2":"0", "0":"5", "5":"2"}
for i in range(N):
    if (brother[i] == "0" and sister[i] == "2") or (brother[i] == "2" and sister[i] == "5") or (brother[i] == "5" and sister[i] == "0"):
        status = "Won"
        Round = i+1
        break
    if (brother[i] == "2" and sister[i] == "0") or (brother[i] == "5" and sister[i] == "2") or (brother[i] == "0" and sister[i] == "5"):
        status = "Lost"
        Round = i+1
        break
    if i == N-1:
        break
    if i >= 1 and sister[i-1] == sister[i]:
        brother.append(opposite[sister[i]])
    else:
        brother.append(sister[i])

print(f"{' '.join(brother)} : {status} at round {Round}")
