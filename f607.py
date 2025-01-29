def binary_search(stick, c):
    left = 0
    right = len(stick)
    while left < right:
        mid = (right + left)//2
        if stick[mid] < c:
            left = mid+1
        else:
            right = mid
    return left
n, L = map(int, input().split())
cuts = [0]*n
for _ in range(n):
    x,i = map(int, input().split())
    cuts[i-1] = x
total = 0
stick = [0, L]
for c in cuts:
    idx = binary_search(stick, c)
    stick.insert(idx, c)
    total += stick[idx+1] - stick[idx-1]
print(total)

    
    
            
