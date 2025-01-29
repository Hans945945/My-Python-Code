n2w = list("mjqhofawcpnsexdkvgtzblryui")
w2n = list("uzrmatifxopnhwvbslekycqjgd")
n = int(input())
for _ in range(n):
    test = input().split()
    m = int(test.pop(0))
    if test[0].isalpha():
        r = [w2n.index(test[i])+1 for i in range(m)]
        print(sum(r))
    else:
        r = [n2w[int(test[i])-1] for i in range(m)]
        print(''.join(r))
