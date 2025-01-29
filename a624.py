import sys
for s in sys.stdin:
    password = s.rstrip()
    score = 0
    if len(password)>= 8:
        score+= 1
    words_only = "".join(char for char in password if char.isalpha())
    if words_only != password and words_only != "":
        score +=1 
    password = words_only
    old = password
    all_lower = password.lower()
    all_upper = password.upper()
    if old != all_lower and old != all_upper:
        score += 1
        
    if score == 3:
        print("This password is STRONG")
    elif score == 2:
        print("This password is GOOD")
    elif score == 1:
        print("This password is ACCEPTABLE")
    else:
        print("This password is WEAK")
