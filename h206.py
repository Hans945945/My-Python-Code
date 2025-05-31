def solve(l, r, is_max):
    if l == r:
        return arr[l]
    mid = (l + r) // 2
    left = solve(l, mid, not is_max)
    right = solve(mid + 1, r, not is_max)
    if is_max:
        return max(left, right)
    else:
        return min(left, right)

n = int(input())
arr = list(map(int, input().split()))
print(solve(0, len(arr) - 1, True))
