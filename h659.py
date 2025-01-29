K,W,S,E = map(int, input().split())
cost = 20
if K > 2:
    cost += 5*(K-2)
cost += (W//2)*5
if S <= 18 and E >= 19:
    cost += 185
if S <= 19 and E >= 20:
    cost += 195
if S <= 20 and E >= 21:
    cost += 205
if S <= 21 and E >= 22:
    cost += 215
if S <= 22 and E >= 23:
    cost += 225
print(cost)
    
    
