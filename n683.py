n = int(input())
for _ in range(n):
    k, w = map(int, input().split())
    words = [input()for _ in range(w)]

    ans = k
    last = words.pop(0)
    for word in words:
        if word == last:
            continue

        temp = k
        for i in range(k):
            if last[i:] == word[:k-i]:
                temp = i
                break
        ans += temp
        last = word

    print(ans)
