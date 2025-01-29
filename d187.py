times = "12312312312312312341231234"
T = int(input())
for i in range(T):
    words = input()
    hit = 0
    for w in words:
        if w == " ":
            hit += 1
        else:
            hit += int(times[ord(w)-97])
    print(f"Case #{i+1}: {hit}")
