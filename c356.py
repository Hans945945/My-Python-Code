N = int(input())
words = list(input())
n = 0
for i in range(N):
    print(words[i*5+n],end="")
    n+=1
