n = int(input())
nums = list(map(int, input().split()))
word = input()
k = int(input())
for _ in range(k):
    temp = []
    for n in nums:
        temp.append(word[n-1])
    word = "".join(temp)
print(word)
