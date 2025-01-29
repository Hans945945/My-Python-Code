#fast
#from collections import Counter
#while True:
    #try:
        #n = int(input())
        #r = sorted(Counter(map(int, input().split())).items(), key=lambda x: (-x[1], x[0]))
        #print(" ".join(map(str, [k for k,_ in r])))
    #except EOFError:
        #break
#fastest
from collections import Counter
while True:
    try:
        n = int(input())
        counts = Counter(map(int, input().split()))
        result = sorted(counts, key=lambda x: (-counts[x], x))
        print(" ".join(map(str, result)))
    except EOFError:
        break


