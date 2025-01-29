code = {"0 1 0 1":"A", "0 1 1 1":"B", "0 0 1 0":"C", "1 1 0 1":"D", "1 0 0 0":"E", "1 1 0 0":"F"}
while True:
    try:
        n = int(input())
        string = ""
        for i in range(n):
            s = input()
            string += code[s]
        print(string)
    except:
        break

        
