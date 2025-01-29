while True:
    try:
        nums = []
        for i in range(int(input())):
            if i <= 1:
                nums.append(i+1)
            else:
                nums.append(nums[i-2]+nums[i-1])
        print(nums[-1])          
    except:
        break

#MAX = 10000
#table = [0 for _ in range(MAX)]

#table[0] = 1
#table[1] = 2

#for i in range(2, MAX):
    #table[i] = table[i-1] + table[i-2]
#while True:
    #try:
        #n = int(input())
        #print(table[n-1])
    #except EOFError:
        #break
