import sys

def c_mod(x, m):
    return x % m if x >= 0 else x % m - m if x % m != 0 else 0
def sort_key(x, m):
    return (c_mod(x, m), 0 if x % 2 == 1 else 1, -x if x % 2 == 1 else x)

data = sys.stdin.readlines()
idx = 0
r = []
while idx < len(data):
    n,m = map(int, data[idx].split())
    if n == 0 and m == 0:
        r.append("0 0")
        break
    idx += 1
    nums = [int(data[idx+i]) for i in range(n)]
    idx += n
    nums.sort(key=lambda x: sort_key(x, m))
    r.append(f"{n} {m}")
    r.extend(nums)
    
sys.stdout.write("\n".join(map(str, r))+"\n")
