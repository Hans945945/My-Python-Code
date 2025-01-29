while True:
    try:
        words = list(input())
        count = 0
        best_count = 0
        best_s = ""
        for i in range(len(words)-1):
            count = count +1
            if words[i] != words[i+1]:
                if count > best_count:
                    best_count = count
                    best_s = words[i]
                count = 0
        count+=1
        if count > best_count:
            best_count = count
            best_s = words[i]

        print(best_s,best_count)
    except:
        break
