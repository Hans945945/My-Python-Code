r = {'e':'q','d':'a','c':'z','r':'w','f':'s','v':'x','t':'e','g':'d','b':'c','y':'r','h':'f','n':'v','u':'t','j':'g','m':'b','i':'y','k':'h',',':'n','o':'u','l':'j','.':'m','p':'i',';':'k','/':',','[':'o',"'":'l',']':'p','2':'`','3':'1','4':'2','5':'3','6':'4','7':'5','8':'6','9':'7','0':'8','-':'9','=':'0','\\':'[', ' ':' '}
while True:
    try:
        words = list(input())
        words = [r[words[i]] for i in range(len(words))]
        print(''.join(words))
    except EOFError:
        break

    



                                                                                                                                                                
                                                                                                                                                                      
