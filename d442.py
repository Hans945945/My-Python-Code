import sys
data = sys.stdin.read().splitlines()
N = int(data[0])
r = []
for x in range(1, N+1):
    original = data[x]
    nums = map(int, list(original))
    while True:
        nums = sum([n*n for n in nums])
        if nums == 16:
            r.append(f"Case #{x}: {original} is an Unhappy number.")
            break
        if nums == 1:
            r.append(f"Case #{x}: {original} is a Happy number.")
            break
        nums = map(int, list(str(nums)))
sys.stdout.write("\n".join(r)+"\n")
    
