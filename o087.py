def Evaluate(Name: str):                       
    if(type(Name) != str):                     
        return -1                              
                                               
    Score = 0                                  
    NameLen = len(Name)                        
                                               
    for i in range(NameLen):                   
        CharCode = ord(Name[i])                
        Score += ((CharCode * 1123) % 1002)    
                                               
        while (CharCode > 0):                  
            Score += (CharCode % 10)           
            CharCode = (CharCode // 10)        
                                               
    return (Score % 101)
n = int(input())
name = []
score = []
for i in range(n):
    name.append(input())
    score.append(Evaluate(name[i]))
for i in range(n-1):
    for j in range(n-i-1):
        if score[j]>score[j+1]:
            temp = score[j]
            score[j] = score[j+1]
            score[j+1] = temp
            temp = name[j]
            name[j] = name[j+1]
            name[j+1] = temp
for i in range(n):
    print(name[i],score[i])

