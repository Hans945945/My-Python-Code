import sys
data = sys.stdin.read().splitlines()
N = data[0]
for i in range(1,len(data)):
    sys.stdout.write(f"Case {i} :\n")
    M, K = map(int, data[i].split())
    a = M//K
    for j in range(1,K):
        sys.stdout.write(f"第{j}位 : 拿{a}元並說DD! BAD!\n")
    sys.stdout.write(f"第{K}位 : 拿{M%K+a}元並說DD! BAD!\n")

    
