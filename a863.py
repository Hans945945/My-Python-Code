while True:
    try:
        original = input().replace('\r', "")
        n = list(map(int, list(original)))
        while True:
            total = 0
            for i in range(len(n)):
                 total += n[i]**2
            n = list(map(int, list(str(total))))
            if n == [1]:
                 print(f"{original} is a happy number")
                 break
            if n == [4]:
                print(f"{original} is an unhappy number")
                break
    except EOFError:
        break
