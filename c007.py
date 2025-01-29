count = 0 
try: 
    while True: 
        n = input()
        for i in n: 
            if i == '"': 
                count +=1 
                if count % 2 == 0: 
                    print("''", end = "") 
                else: 
                    print("``", end = "") 
            else: 
                print(i, end = "") 
        print() 
except EOFError: 
     pass
