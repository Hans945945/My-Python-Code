import itertools
while True:
    try:
        n = int(input())

        nums = [str(i) for i in range(1,n+1)]

        permutations = list(itertools.permutations(nums))

        permutations = ["".join(p) for p in permutations]
        permutations.sort(reverse = True)

        for perm in permutations:
            print(perm)
    except:
        break
