p1 = {}
N = int(input())
nums1 = list(map(int, input().split()))
for i in range(0, N*2, 2):
    p1[nums1[i]] = nums1[i+1]
p2 = {}
N = int(input())
nums2 = list(map(int, input().split()))
for i in range(0, N*2, 2):
    p2[nums2[i]] = nums2[i+1]

result = p1.copy()
for key, value in p2.items():
    result[key] = result.get(key, 0) + value
r = []
for key, value in sorted(result.items(), reverse = True):
    if value != 0: r.append(f"{key}:{value}")

print("\n".join(r) if r else "NULL!")
