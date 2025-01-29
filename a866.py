r = int(input())
rating = [0,0,0,0,0,0]
total = 0
while r != 0:
    rating[r] += 1
    total += r
    r = int(input())
for i in range(5,0,-1):
    rate = rating[i]
    if rate < 10:
        rate = " "+str(rate)
    string = "".join('=' for j in range(rating[i]))
    print(f"{i} ({rate}) |{string}")
avg = round(total / sum(rating),4)
print(f"Average rating: {avg:.4f}")
